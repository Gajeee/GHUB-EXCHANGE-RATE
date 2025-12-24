# Ghub Exchange

![Python](https://img.shields.io/badge/Python-3.x-4B8BBE?style=for-the-badge&logo=python&logoColor=white&color=000000) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-33B8FF?style=for-the-badge&logo=python&logoColor=white&color=000000) ![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-FF6F61?style=for-the-badge&logo=requests&logoColor=white&color=000000) ![Pytz](https://img.shields.io/badge/Pytz-Time%20Zones-F4B400?style=for-the-badge&logo=python&logoColor=white&color=000000)

Ghub Exchange is a lightweight and minimal currency exchange rate tracker that runs in the background. It provides real-time exchange rate data and local time information for selected countries. It also displays how the exchange rates have changed over the past 24 hours, making it an efficient tool for tracking currency fluctuations in an easy-to-read interface.

## Features

- **Real-time Exchange Rates**: View exchange rates for MYR, SGD, USD, and CNY.
- **Local Time Tracking**: Displays the local time for Malaysia, Singapore, New York, and China.
- **24-Hour Exchange Rate History**: Tracks and shows how exchange rates have changed in the past 24 hours with up or down indicators.
- **Minimalistic UI**: Simple and clean interface for easy access to the information you need.
- **Background Running**: The app runs in the background, periodically updating the exchange rates and time.

## How It Works

The app fetches exchange rate data from a public API (Exchangerate-API) and displays the rates for MYR, SGD, USD, and CNY, relative to USD. It also shows the local time for Malaysia, Singapore, New York, and China. The app automatically updates these values every second.

1. **Exchange Rates**: It fetches the latest exchange rates for MYR, SGD, USD, and CNY.
2. **Time**: Displays the local time for four different countries using time zones.
3. **24-Hour History**: Tracks and compares the current exchange rate with the value from 24 hours ago to show the movement (⇡ or ⇣).
4. **UI**: The information is shown in a clean and easy-to-read format using a GUI with tables for exchange rates and time.

## UI Screenshots

Below are screenshots of the app's user interface:

<table>
  <tr>
    <td><img src="images/ui1.jpg" width="500" alt="UI Screenshot 1" style="padding: 10px;"></td>
    <td><img src="images/ui2.jpg" width="500" alt="UI Screenshot 2" style="padding: 10px;"></td>
  </tr>
</table>

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/ghub-exchange.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python Ghub_Exchange.py
    ```

## Requirements

- ![Python](https://img.shields.io/badge/Python-3.x-4B8BBE?style=for-the-badge&logo=python&logoColor=white&color=000000) Python 3.x
- ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-33B8FF?style=for-the-badge&logo=python&logoColor=white&color=000000) Tkinter (for GUI)
- ![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-FF6F61?style=for-the-badge&logo=requests&logoColor=white&color=000000) Requests (for fetching exchange rates)
- ![Pytz](https://img.shields.io/badge/Pytz-Time%20Zones-F4B400?style=for-the-badge&logo=python&logoColor=white&color=000000) Pytz (for time zone handling)

