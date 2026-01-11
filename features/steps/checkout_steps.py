from behave import given, when, then
from playwright.sync_api import expect

# --- PRECONDITIONS (GIVEN) ---
@given('the user is logged in and has items in the cart')
def step_impl(context):
    # ใช้ Logic การ Login ของคุณที่นี่
    context.page.goto("https://www.saucedemo.com/")
    context.page.fill("#user-name", "standard_user")
    context.page.fill("#password", "secret_sauce")
    context.page.click("#login-button")
    context.page.click("#add-to-cart-sauce-labs-backpack") # เพิ่มของ
    context.page.click(".shopping_cart_link") # ไปที่ตะกร้า
    context.page.click("#checkout") # กด Checkout

@given('the user is on the checkout information page')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

# --- ACTIONS (WHEN) ---
@when('the user enters valid checkout details')
def step_impl(context):
    context.page.fill("#first-name", "John")
    context.page.fill("#last-name", "Doe")
    context.page.fill("#postal-code", "12345")

@when('clicks the continue button')
def step_impl(context):
    context.page.click("#continue")

@when('the user enters details but leaves postal code empty')
def step_impl(context):
    context.page.fill("#first-name", "John")
    context.page.fill("#last-name", "Doe")
    context.page.fill("#postal-code", "")

# --- ASSERTIONS (THEN) ---
@then('the checkout overview page should be displayed')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

@then('an error message "{error_text}" should be shown')
def step_impl(context, error_text):
    error_locator = context.page.locator("[data-test='error']")
    expect(error_locator).to_contain_text(error_text)
    
    # --- ส่วนที่เพิ่มสำหรับ Scenario 2: User cancels checkout ---
@when('the user clicks the cancel button')
def step_impl(context):
    context.page.click("#cancel")

@then('the cart page should be displayed')
def step_impl(context):
    expect(context.page).to_have_url("https://www.saucedemo.com/cart.html")

# --- ส่วนที่เพิ่มสำหรับ Scenario 4: Special characters ---
# หมายเหตุ: Step นี้จะจับคู่กับประโยคใน Feature File ที่เราเขียนว่า
# When the user enters "O'Neil-Smith" as the first name
@when('the user enters "O\'Neil-Smith" as the first name')
def step_impl(context):
    context.page.fill("#first-name", "O'Neil-Smith")
    context.page.fill("#last-name", "Doe")
    context.page.fill("#postal-code", "12345")