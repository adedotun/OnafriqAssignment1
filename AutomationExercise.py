import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
browser = webdriver.Chrome()


def remove_iframes(driver):
    """ Remove any iframe advertisements that may obstruct clicks. """
    try:
        # Find all iframes and remove them from the DOM
        ad_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in ad_iframes:
            driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", iframe)
    except Exception as e:
        print(f"Could not remove the ad iframe: {e}")


def js_click(driver, element):
    """ Use JavaScript to click an element. """
    driver.execute_script("arguments[0].click();", element)


browser.get("https://www.automationexercise.com/")
sign_in_button = browser.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
sign_in_button.click()

username = browser.find_element(By.NAME, "email")
password = browser.find_element(By.NAME, "password")

username.send_keys("qat@mailinator.com")
password.send_keys("123456")

login_button = browser.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_button.click()

browser.implicitly_wait(10)
# Find the featured items section
featured_items = (
    browser.find_elements(By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']"))

# Extract labels and prices
items = []
for item in featured_items:
    try:
        price = item.find_element(By.TAG_NAME, "h2").text
        label = item.find_element(By.TAG_NAME, "p").text
        # converted to float for easy sorting
        price_value = float(price.replace("Rs. ", "").strip())
        items.append((label, price_value))
    except Exception as e:
        print(f"Error processing item: {e}")

# Sort items by price (low to high)
sorted_items = sorted(items, key=lambda x: x[1])

# Print sorted items after converting back to int
for label, price in sorted_items:
    print(f"Label: {label}  &   Price: Rs. {int(price)}")

# Navigate to Women >> Dress >> Women – Tops Products
women_menu = browser.find_element(By.XPATH, "//a[normalize-space()='Women']")
try:
    js_click(browser, women_menu)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, women_menu)

browser.implicitly_wait(10)

women_tops_menu = browser.find_element(By.XPATH, "//a[normalize-space()='Tops']")
try:
    js_click(browser, women_tops_menu)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, women_tops_menu)

# Wait for the Women - Tops Products page to load
browser.implicitly_wait(10)  # seconds

# Find the Fancy Green Top and add to cart
fancy_green_top = browser.find_element(By.XPATH, "//p[contains(text(), 'Fancy Green Top')]/ancestor::div["
                                                 "@class='productinfo text-center']")
try:
    js_click(browser, fancy_green_top.find_element(By.CLASS_NAME, "add-to-cart"))
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, fancy_green_top.find_element(By.CLASS_NAME, "add-to-cart"))


# Handle the modal for adding to cart
browser.implicitly_wait(5)  # seconds
continue_shopping = browser.find_element(By.CLASS_NAME, "close-modal")
try:
    js_click(browser, continue_shopping)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, continue_shopping)
# continue_shopping.click()

# Add Summer White Top to cart
summer_white_top = browser.find_element(By.XPATH, "//p[contains(text(), 'Summer White Top')]/ancestor::div["
                                                  "@class='productinfo text-center']")
try:
    js_click(browser, summer_white_top.find_element(By.CLASS_NAME, "add-to-cart"))
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, summer_white_top.find_element(By.CLASS_NAME, "add-to-cart"))


# Handle the modal for adding to cart
browser.implicitly_wait(5)  # seconds
continue_shopping = browser.find_element(By.CLASS_NAME, "close-modal")
try:
    js_click(browser, continue_shopping)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, continue_shopping)

# View cart
view_cart_button = browser.find_element(By.XPATH, "//a[normalize-space()='Cart']")
try:
    js_click(browser, view_cart_button)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, view_cart_button)


# Wait for the page to load
browser.implicitly_wait(10)  # seconds

# Proceed to checkout
proceed_to_checkout_button = browser.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")
try:
    js_click(browser, proceed_to_checkout_button)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, proceed_to_checkout_button)


# Wait for the page to load
browser.implicitly_wait(10)  # seconds

# Add comment
comment_area = browser.find_element(By.NAME, "message")
comment_area.send_keys("Order placed.")

# Click on Place Order
place_order_button = browser.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")
try:
    js_click(browser, place_order_button)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, place_order_button)


# Wait for the page to load
browser.implicitly_wait(10)  # seconds

# Enter card details
name_on_card = browser.find_element(By.NAME, "name_on_card")
card_number = browser.find_element(By.NAME, "card_number")
cvc = browser.find_element(By.NAME, "cvc")
expiry_month = browser.find_element(By.NAME, "expiry_month")
expiry_year = browser.find_element(By.NAME, "expiry_year")

name_on_card.send_keys("Test Card")
card_number.send_keys("4100000000000000")
cvc.send_keys("123")
expiry_month.send_keys("01")
expiry_year.send_keys("1900")

# Click on Pay and Confirm Order
pay_and_confirm_button = browser.find_element(By.XPATH, "//button[@id='submit']")
try:
    js_click(browser, pay_and_confirm_button)
    browser.implicitly_wait(10)
except Exception as e:
    print(f"Click intercepted: {e}")
    remove_iframes(browser)
    js_click(browser, pay_and_confirm_button)

# Wait for the confirmation page to load
WebDriverWait(browser, 10)

body_text = browser.find_element(By.TAG_NAME, "body").text

# Try to find the confirmation message
try:
    confirmation_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          '//p[normalize-space()=\'Congratulations! Your order has been confirmed!\']')))
    print("Order Confirmation: ", confirmation_message.text)
except Exception as e:
    print(f"Could not find the confirmation message: {e}")

# Close the browser
time.sleep(10)
browser.quit()
