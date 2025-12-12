import tkinter as tk
from tkinter import messagebox
import requests

# City coordinates
city_coords = {
    "Tehran": (35.6892, 51.3890),
    "Mashhad": (36.2605, 59.6168),
    "Isfahan": (32.6546, 51.6680),
    "Shiraz": (29.5918, 52.5836),
    "Tabriz": (38.0800, 46.2919),
    "Karaj": (35.8400, 50.9391),
}

# Weather code mapping to human-readable text
weather_desc = {
    0: "Clear", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Rime Fog", 51: "Light drizzle", 53: "Moderate drizzle",
    55: "Heavy drizzle", 61: "Light rain", 63: "Rain", 65: "Heavy rain",
    71: "Snow", 73: "Snow", 75: "Heavy snow", 80: "Rain showers",
    81: "Moderate showers", 82: "Heavy showers", 95: "Thunderstorm",
    96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail"
}

def get_weather():
    city = city_entry.get()
    if city not in city_coords:
        messagebox.showerror("Error", "City not found!")
        return

    lat, lon = city_coords[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()
        current = data["current_weather"]
        temp = current["temperature"]
        wind = current["windspeed"]
        code = current["weathercode"]
        desc = weather_desc.get(code, "Unknown")
        result_label.config(text=f"{city}\n{temp}°C\n{desc}\nWind: {wind} km/h")
    except:
        messagebox.showerror("Error", "Cannot fetch weather data!")

# Tkinter UI
root = tk.Tk()
root.title("Weather App")
root.geometry("360x240")
root.configure(bg="#e0f7fa")

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=15)

get_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), bg="#00acc1", fg="white", command=get_weather)
get_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#e0f7fa", fg="#006064")
result_label.pack(pady=15)

root.mainloop()
