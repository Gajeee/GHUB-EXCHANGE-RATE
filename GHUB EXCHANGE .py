import requests
from datetime import datetime, timedelta
import pytz
import tkinter as tk
from tkinter import ttk
import random

# Global variables for storing exchange rate history
currency_history = {
    "MYR": [],
    "SGD": [],
    "USD": [],
    "CNY": []
}

# Function to fetch currency exchange rates based on USD
def fetch_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200:
            usd_to_rates = {
                "MYR (Ringgit)": data['rates']['MYR'],
                "SGD (Dollar)": data['rates']['SGD'],
                "USD (Dollar)": 1,  # USD to USD rate is always 1
                "CNY (Yen)": data['rates']['CNY'],
            }
            return usd_to_rates
        else:
            return {"Error": "Error fetching exchange rates."}
    except Exception as e:
        return {"Error": f"Error: {e}"}

# Function to get the current time in different countries
def get_time():
    timezones = {
        "Malaysia": "Asia/Kuala_Lumpur",
        "Singapore": "Asia/Singapore",
        "New York": "America/New_York",
        "China": "Asia/Shanghai"
    }

    time_data = []
    for country, timezone in timezones.items():
        tz = pytz.timezone(timezone)
        local_time = datetime.now(tz)
        time_data.append([country, local_time.strftime('%H:%M:%S')])
    
    return time_data

# Function to update the GUI with the latest time and exchange rate data
def update_gui(window):
    time_data = get_time()
    exchange_data = fetch_exchange_rate()

    # Update Time section
    update_time_table(window, time_data)
    update_exchange_rate_table(window, exchange_data)
    update_time_diff_table(window)

    # Schedule the next update
    window.after(1000, update_gui, window)

# Function to update the time table in the GUI
def update_time_table(window, time_data):
    for row in window.time_table.get_children():
        window.time_table.delete(row)
    
    for row in time_data:
        window.time_table.insert("", "end", values=row)

# Function to update the exchange rate table in the GUI
def update_exchange_rate_table(window, exchange_data):
    for row in window.exchange_table.get_children():
        window.exchange_table.delete(row)

    if "Error" in exchange_data:
        window.exchange_table.insert("", "end", values=("Error", exchange_data["Error"]))
    else:
        prev_rates = {"MYR": 4.0000, "SGD": 1.3000, "USD": 3.2000, "CNY": 9.5000}  # Example previous rates

        for currency, rate in exchange_data.items():
            prev_rate = prev_rates.get(currency.split(' ')[0], 1)
            arrow = ""
            if rate > prev_rate:
                arrow = " ⇡"
            elif rate < prev_rate:
                arrow = " ⇣"

            # Simulating a small movement in the rate (moving decimal)
            moving_rate = rate + random.uniform(-0.001, 0.001)  # Adding a small random fluctuation

            window.exchange_table.insert("", "end", values=(currency, f"{moving_rate:.4f}{arrow}"))

        # Add the new exchange rates to the currency history
        for currency, rate in exchange_data.items():
            currency_code = currency.split(' ')[0]
            if currency_code in currency_history:
                currency_history[currency_code].append(rate)
                if len(currency_history[currency_code]) > 24:  # Keep only the last 24 values (hours)
                    currency_history[currency_code].pop(0)

# Function to update the table showing exchange rates 24 hours ago
def update_time_diff_table(window):
    window.time_diff_table.delete(*window.time_diff_table.get_children())  # Clear previous rows

    for currency_code in currency_history:
        rates = currency_history[currency_code]
        if len(rates) >= 2:  # Ensure there are at least 2 rates (current + past)
            rate_24_hours_ago = rates[0]  # Rate from 24 hours ago
            rate_now = rates[-1]  # Current rate
            arrow = "⇡" if rate_now > rate_24_hours_ago else "⇣"
            
            window.time_diff_table.insert("", "end", values=(currency_code, f"{rate_24_hours_ago:.4f} {arrow}"))

# Function to create and display the main window
def create_window():
    window = tk.Tk()
    window.title("Ghub Exchange")
    window.configure(bg="black")  # Set black background
    window.geometry("400x500")  # Adjusted window size to fit new table

    # Top title text (App name in the center)
    title_label = tk.Label(window, text="Ghub Exchange", fg="white", bg="black", font=("Courier", 14, "bold"))
    title_label.pack(pady=10)

    # Main frame for content
    frame = tk.Frame(window, bg="black")
    frame.pack(fill=tk.BOTH, expand=True)

    # Time table with larger font size
    window.time_table = ttk.Treeview(frame, columns=("Country", "Local Time"), show="headings", height=4)
    window.time_table.heading("Country", text="Country", anchor=tk.W)
    window.time_table.heading("Local Time", text="Local Time", anchor=tk.W)
    window.time_table.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # Exchange rates table with larger font size
    window.exchange_table = ttk.Treeview(frame, columns=("Currency", "Exchange Rate"), show="headings", height=4)
    window.exchange_table.heading("Currency", text="Currency", anchor=tk.W)
    window.exchange_table.heading("Exchange Rate", text="Exchange Rate", anchor=tk.W)
    window.exchange_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    # Time difference table (24 hours ago with arrows)
    window.time_diff_table = ttk.Treeview(frame, columns=("Currency", "24 Hours Ago"), show="headings", height=4)
    window.time_diff_table.heading("Currency", text="Currency", anchor=tk.W)
    window.time_diff_table.heading("24 Hours Ago", text="24 Hours Ago", anchor=tk.W)
    window.time_diff_table.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

    # Footer: Made by Gajee (smaller text at the bottom)
    footer_label = tk.Label(window, text="Made by Gajee", fg="white", bg="black", font=("Courier", 8))
    footer_label.pack(side=tk.BOTTOM, pady=10)

    # Start updates
    update_gui(window)

    window.mainloop()

# Run the application
if __name__ == "__main__":
    create_window()
