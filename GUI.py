import asyncio
import sys

import PySimpleGUI as sg

# bluetooth.py>
sg.theme('Black')  # Set the color scheme

avg_temp = [sg.Text(text="Avg Temp\n\n _ _ _ °F", justification="center", border_width=6, key="Avg Temp",
                    background_color="white", font=("Helvetica", 15), size=(10, 4), text_color="black")]
max_temp = [sg.Text(text="Max Temp\n\n _ _ _ °F", justification="center", border_width=6, key="Max Temp",
                    background_color="white", font=("Helvetica", 15), size=(10, 4), text_color="black")]
current_temp = [sg.Text(text="Curr Temp\n\n _ _ _ °F", justification="center", border_width=6, key="Curr Temp",
                        background_color="white", font=("Helvetica", 15), size=(10, 4), text_color="black")]

buttons = [sg.Button("Start/Stop", font=("Helvetica", 15), pad=(5, 5)),
           sg.Button("°C/°F", font=("Helvetica", 15), pad=(5, 5)),
           sg.Button("Quit", font=("Helvetica", 15), pad=(5, 5))]

total_temp = [max_temp, avg_temp, current_temp]

maxT = -sys.maxsize - 1
current_temp = None

total_temp = 0
num_temps = 0
avgT = 0

in_celsius = False
poll = False
layout = [
    [sg.Column([buttons], vertical_alignment="bottom"),
     sg.Column(total_temp, vertical_alignment="bottom")]]


def update_value(key: str, value: float, celsius: bool):
    if celsius:
        window[key].update(f"{key}\n\n {value} °C")
    else:
        window[key].update(f"{key}\n\n {value} °F")
    window.refresh()


def change_unit(value, celsius):
    if celsius:
        return round((value * 9 / 5) + 32, 2)
    return round((value - 32) * 5 / 9, 2)


window = sg.Window(title='Autonomous Vehicle GUI', layout=layout)  # Create the window with the title and layout

while True:
    event, values = window.read()  # Read events and values from the window
    if event == sg.WIN_CLOSED or event == "Quit":  # If the user closes the window
        break  # Exit the loop and close the window
    if event == "°C/°F" and current_temp is not None:
        current_temp = change_unit(current_temp, in_celsius)
        maxT = change_unit(maxT, in_celsius)
        avgT = change_unit(avgT, in_celsius)
        in_celsius = not in_celsius
        update_value("Curr Temp", current_temp, in_celsius)
        update_value("Max Temp", maxT, in_celsius)
        update_value("Avg Temp", avgT, in_celsius)


window.close()  # Close the window when the loop exits
