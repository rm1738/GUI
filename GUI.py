import PySimpleGUI as sg
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

layout = [
    [sg.Column([buttons], vertical_alignment="bottom"),
     sg.Column(total_temp, vertical_alignment="bottom")]]

window = sg.Window(title='Autonomous Vehicle GUI', layout=layout)  # Create the window with the title and layout

while True:
    event, values = window.read()  # Read events and values from the window
    if event == sg.WIN_CLOSED:  # If the user closes the window
        break  # Exit the loop and close the window
    elif event == "Quit":  # If the user clicks the quit button
        break  # Exit the loop and close the window

window.close()  # Close the window when the loop exits
