# Report Maker 5.0
# By Wolfnom ~ Sergio A. Knapik
# 2024

import pandas as pd
from datetime import datetime

main_sheet_path = input("Qual o caminho da planilha principal? ")

temp_sheet_paths = list()
humidity_sheet_paths = list()
initial_day = int(input("Qual o dia inicial? (apenas números do dia, sem mês e ano): "))
final_day = int(input("Qual o dia final? (apenas números do dia, sem mês e ano): "))
current_month = int(input("Qual o mês atual? (apenas números do mês): "))

keep_asking = True
while keep_asking:
    user_input = input("Qual o caminho da planilha do sensor? ")
    if "Temperatura(℃)" in pd.read_excel(user_input).columns:
        temp_sheet_paths.append(user_input)
    elif "Humidade atual(%)" in pd.read_excel(user_input).columns:
        humidity_sheet_paths.append(user_input)
    user_stop = input("Deseja adicionar mais uma planilha de sensor? (y / any): ")
    if user_stop != "y":
        keep_asking = False

main_sheet = pd.read_excel(main_sheet_path)
main_sheet["Dia"] = pd.to_datetime(main_sheet["Dia"]).dt.date


def interpolate_data(main_date, sheet, data_column):

    sheet["DateTime"] = pd.to_datetime(sheet["DateTime"])

    sheet["Hour_HH"] = sheet["DateTime"].dt.hour
    sheet.set_index("Hour_HH", inplace=True)

    interpolated_data = list()
    qnt = 0
    for index, row in main_date.iterrows():
        hour = datetime.strptime(row["Hora"], "%H:%M:%S").hour
        initial_value = sheet.loc[hour, data_column]
        next_hour = (hour + 1) % 24
        final_value = sheet.loc[next_hour, data_column]

        time_fraction = ((qnt * 15) / 3600) - 1
        time_int = int(time_fraction)
        time_fraction = time_fraction - time_int

        if data_column == "Temperatura(℃)":
            rounding = 2
        else:
            rounding = 0

        if final_value == initial_value:
            interpolated_value = initial_value
        else:
            interpolated_value = round(initial_value + ((final_value - initial_value) * time_fraction), rounding)

        if interpolated_value <= 0:
            interpolated_value = initial_value
        interpolated_data.append(interpolated_value)

        qnt += 1

    return interpolated_data


sheet_day_index = 0
for day in range(initial_day, final_day+1):
    main_day = main_sheet[main_sheet["Dia"] == datetime(2024, current_month, day).date()]

    current_temp_sheet = pd.read_excel(temp_sheet_paths[sheet_day_index])

    current_humidity_sheet = pd.read_excel(humidity_sheet_paths[sheet_day_index])

    main_day["Temperatura"] = interpolate_data(main_date=main_day,
                                               sheet=current_temp_sheet,
                                               data_column="Temperatura(℃)")
    main_day["Umidade"] = interpolate_data(main_date=main_day,
                                           sheet=current_humidity_sheet,
                                           data_column="Humidade atual(%)")
    main_sheet.update(main_day)
    sheet_day_index += 1

user_save = input("Onde deseja salvar a planilha de resultado? ")
main_sheet.to_excel(user_save, index=False)

print("Feito!")
