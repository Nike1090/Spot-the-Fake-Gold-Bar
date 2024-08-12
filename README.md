# Fake Gold Bar Detection using Python Selenium

## Project Overview

This project is a Python script that automates the process of finding a fake gold bar out of 9 gold bars using the Selenium WebDriver. The script interacts with a web page, performs weighings of different groups of gold bars, and identifies the fake bar through a divide and conquer approach.

## Features

- **Automated Web Interaction:** Uses Selenium to interact with web elements.
- **Divide and Conquer Strategy:** Implements a ternary search strategy to efficiently identify the fake gold bar.
- **Alert Handling:** Captures and handles alerts that indicate the fake gold bar's identity.
- **Weighing Results Logging:** Logs the number of weighings and the results for analysis.

## Installation

### Prerequisites

- Python 3.x
- Selenium WebDriver
- A browser driver (e.g., GeckoDriver for Firefox, ChromeDriver for Chrome)

### Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Nike1090/Spot-the-Fake-Gold-Bar.git
    cd Spot-the-Fake-Gold-Bar
    ```

2. **Install Dependencies:**
    Install the required Python packages using pip:
    ```bash
    pip install selenium
    ```

3. **Download and Setup WebDriver:**
   - For Firefox, download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and ensure it is accessible in your system's PATH.
   - For Chrome, download [ChromeDriver](https://sites.google.com/chromium.org/driver/) if using Chrome and update the `initialize_driver()` function accordingly.

## Usage

1. **Run the Script:**
   ```bash
   python main.py
