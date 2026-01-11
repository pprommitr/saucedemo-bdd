Feature: Checkout Workflow

  Background:
    Given the user is logged in and has items in the cart
    And the user is on the checkout information page

  Scenario: Successful checkout with valid information
    When the user enters valid checkout details
    And clicks the continue button
    Then the checkout overview page should be displayed

  Scenario: User cancels checkout
    When the user clicks the cancel button
    Then the cart page should be displayed

  Scenario: Checkout fails with empty postal code
    When the user enters details but leaves postal code empty
    And clicks the continue button
    Then an error message "Error: Postal Code is required" should be shown

  Scenario: User completes checkout with special characters in name
    When the user enters "O'Neil-Smith" as the first name
    And clicks the continue button
    Then the checkout overview page should be displayed