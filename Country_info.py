# country_info_app.py
import requests
from tkinter import *
from tkinter import messagebox

# ---------------------------- FUNCTIONS ------------------------------- #
def get_country_info():
    country_name = entry.get().strip()
    if not country_name:
        messagebox.showerror("Input Error", "Please enter a country name.")
        return

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]

        capital = data.get("capital", ["N/A"])[0]
        region = data.get("region", "N/A")
        population = data.get("population", "N/A")
        currency = list(data.get("currencies", {"N/A": {"name": "N/A"}}).values())[0]['name']
        languages = ", ".join(data.get("languages", {"N/A": "N/A"}).values())

        result_text.set(
            f"Capital: {capital}\n"
            f"Region: {region}\n"
            f"Population: {population:,}\n"
            f"Currency: {currency}\n"
            f"Languages: {languages}"
        )
        entry.delete(0, END)  # Clear the entry field after fetching data
    except requests.exceptions.HTTPError:
        messagebox.showerror("Not Found", f"No information found for '{country_name}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Country Info Finder")
window.config(padx=40, pady=40, bg="#B1DDC6")

Label(window, text="Enter Country Name:", font=("Arial", 12, "bold"), bg="#B1DDC6").pack()

entry = Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=10)
entry.focus()

Button(window, text="Get Info", font=("Arial", 12), command=get_country_info).pack(pady=5)

result_text = StringVar()
Label(window, textvariable=result_text, font=("Arial", 11), bg="#B1DDC6", justify=LEFT).pack(pady=10)

window.mainloop()
