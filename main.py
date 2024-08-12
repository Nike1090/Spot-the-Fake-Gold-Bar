from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert 
import time
import sys

# Main function
def main():
    try:
        driver = initialize_driver()
        elements, wait = find_elements(driver)
        fake_gold_bar = find_fake_gold_bar(driver, elements, wait)
        
        # Click the button for the fake bar
        driver.find_element(By.ID, f"coin_{fake_gold_bar}").click()
        alert = Alert(driver)
        alert_message = alert.text
        alert.accept()
        
        # Print results
        all_weighings = [ele.text for ele in elements['game_info'].find_elements(By.CSS_SELECTOR, 'ol li')]
        print(f"Fake Gold Bar is: {fake_gold_bar}")
        print(f"Alert Message: {alert_message}")
        print(f"Number of Weighings: {len(all_weighings)}")
        print(f"Weighing List: {all_weighings}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

    # finally:
        # Close the driver
        # driver.quit()

# Initialize the webDriver
def initialize_driver():
    try:
        driver = webdriver.Firefox()
        driver.get("http://sdetchallenge.fetch.com/")
        return driver
    except Exception as e:
        print(f"Error initializing the WebDriver: {e}", file=sys.stderr)
        sys.exit(1)

# Find the elements on the page
def find_elements(driver):
    try:
        wait = WebDriverWait(driver, 100)
        elements = {
            'weigh': driver.find_element(By.ID, 'weigh'),
            'reset': driver.find_element(By.CSS_SELECTOR, 'button#reset:not([disabled])'),
            'left_grid': driver.find_elements(By.CSS_SELECTOR, "input[data-side='left']"),
            'right_grid': driver.find_elements(By.CSS_SELECTOR, "input[data-side='right']"),
            'gold_bars': driver.find_elements(By.CSS_SELECTOR, "button.square"),
            'game_info': wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.game-info')))
        }
        return elements, wait
    except Exception as e:
        print(f"Error finding elements: {e}", file=sys.stderr)
        driver.quit()
        sys.exit(1)

# Perform the weighing and get the results
def perform_weighing(driver, elements, left_bars, right_bars, wait):
    try:
        # Fill the scales
        for index, bar in enumerate(left_bars):
            elements['left_grid'][index].send_keys(bar)
        for index, bar in enumerate(right_bars):
            elements['right_grid'][index].send_keys(bar)
        elements['weigh'].click()
        time.sleep(3)

        weighing_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.game-info > ol')))
        weighing_result_elements = weighing_list.find_elements(By.TAG_NAME, 'li')
        results = [ele.text for ele in weighing_result_elements]
        return results
    except Exception as e:
        print(f"Error performing weighing: {e}", file=sys.stderr)
        driver.quit()
        sys.exit(1)

# Find the fake gold bar via Divide and Conquer approach using ternary Search
def find_fake_gold_bar(driver, elements, wait):
    try:
        all_bars = [str(i) for i in range(9)]
        while len(all_bars) > 1:
            group_size = len(all_bars) // 3
            group1 = all_bars[:group_size]
            group2 = all_bars[group_size:2*group_size]
            remaining = all_bars[2*group_size:]
            elements['reset'].click()
            time.sleep(2)
            # Weigh the two groups
            results = perform_weighing(driver, elements, group1, group2, wait)
            if '>' in results[-1]:
                all_bars = group2
            elif '<' in results[-1]:
                all_bars = group1
            else:
                all_bars = remaining

        return all_bars[0]
    except Exception as e:
        print(f"Error finding the fake gold bar: {e}", file=sys.stderr)
        driver.quit()
        sys.exit(1)

if __name__ == '__main__':
   main()
