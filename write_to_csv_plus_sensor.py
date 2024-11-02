import plant_sensor_lib as plant
import time
import datetime


PLANT = "Totosa"  # Totosa ou Excaulebur
PORT = "COM6"

plant.open_port(PORT)

csv_text = "Valor do sinal,Temperatura,Umidade,Hora,Dia\n"

while True:
    try:
        if plant.available_values():
            plant_signal = plant.get_float()

            current_signal = (f"{plant_signal},_°C,_%,"
                              f"{datetime.datetime.now().strftime("%H:%M:%S")},"
                              f"{datetime.date.today()}\n")
            csv_text += current_signal
            print(current_signal)
            time.sleep(15)

        else:
            time.sleep(0.01)

    except:
        plant.close_port()
        print("Port closed.")
        break

file_name = f"{PLANT}_{datetime.date.today()}.csv"

with open(file_name, "w") as file:
    file.write(csv_text)

print("Feito.")
