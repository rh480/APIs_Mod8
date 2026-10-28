# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests
from playwright.sync_api import expect  # type: ignore[reportMissingImports]  # Auto-waiting assertions for Playwright


# The following decorators and functions define E2E tests for the FastAPI calculator application.

BASE_URL = 'http://localhost:8000'

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto(BASE_URL)
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    expect(page.locator('h1')).to_have_text('Hello World')

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    This test simulates a user performing an addition operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Add" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto(BASE_URL)
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    expect(page.locator('#result')).to_have_text('Calculation Result: 15')

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.
    """
    page.goto(BASE_URL)
 
    page.fill('#a', '10')
    page.fill('#b', '4')
    page.click('button:text("Subtract")')
 
    expect(page.locator('#result')).to_have_text('Calculation Result: 6')
 
 
@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.
    """
    page.goto(BASE_URL)
 
    page.fill('#a', '6')
    page.fill('#b', '7')
    page.click('button:text("Multiply")')
 
    expect(page.locator('#result')).to_have_text('Calculation Result: 42')
 
 
@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """
    Test the division functionality of the calculator.
    """
    page.goto(BASE_URL)
 
    page.fill('#a', '10')
    page.fill('#b', '4')
    page.click('button:text("Divide")')
 
    expect(page.locator('#result')).to_have_text('Calculation Result: 2.5')
 
 
@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.
 
    Fills in the numbers, clicks "Divide", and waits for the error message that the
    API returns (HTTP 400) to be displayed.
    """
    page.goto(BASE_URL)
 
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
 
    expect(page.locator('#result')).to_have_text('Error: Cannot divide by zero!')