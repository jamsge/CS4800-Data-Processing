# IMPORTANT: Column data is different before June 6/1/2014!
# data file is in English units

import os
import csv
import datetime

years_folders = os.listdir("./data")
final_data = {}
cols_1 = {
    "station_id": 0,
    "date": 1,
    "julian_date": 2,
    "qc_solar_radiation_average": 3,
    "solar_radiation_average": 4,
    "qc_average_soil_temp": 5,
    "average_soil_temp": 6,
    "qc_max_air_temp": 7,
    "max_air_temp": 8,
    "qc_min_air_temp": 9,
    "min_air_temp": 10,
    "qc_average_air_temp": 11,
    "average_air_temp": 12,
    "qc_average_vapor_pressure": 13,
    "average_vapor_pressure": 14,
    "qc_average_wind_speed": 15,
    "average_wind_speed": 16,
    "qc_precipitation": 17,
    "precipitation": 18,
    "qc_max_relative_humidity": 19,
    "max_relative_humidity": 20,
    "qc_min_relative_humidity": 21,
    "min_relative_humidity": 22,
    "qc_reference_eto": 23,
    "reference_eto": 24,
    "qc_average_relative_humidity":25,
    "average_relative_humidity": 26,
    "qc_dew_point": 27,
    "dew_point": 28,
    "qc_wind_run": 29,
    "wind_run": 30
}

cols_2 = {
    "station_id": 0,
    "date": 1,
    "julian_date": 2,
    "reference_eto": 3,
    "qc_reference_eto": 4,
    "precipitation": 5,
    "qc_precipitation": 6,
    "solar_radiation_average": 7,
    "qc_solar_radiation_average": 8,
    "average_vapor_pressure": 9,
    "qc_average_vapor_pressure": 10,
    "max_air_temp": 11,
    "qc_max_air_temp": 12,
    "min_air_temp": 13,
    "qc_min_air_temp": 14,
    "average_air_temp": 15,
    "qc_average_air_temp": 16,
    "max_relative_humidity": 17,
    "qc_max_relative_humidity": 18,
    "min_relative_humidity": 19,
    "qc_min_relative_humidity": 20,
    "average_relative_humidity": 21,
    "qc_average_relative_humidity":22,
    "dew_point": 23,
    "qc_dew_point": 24,
    "average_wind_speed": 25,
    "qc_average_wind_speed": 26,
    "wind_run": 27,
    "qc_wind_run": 28,
    "average_soil_temp": 29,
    "qc_average_soil_temp": 30,
}



for year in years_folders:
    files = os.listdir(f"./data/{year}")
    for file in files:
        with open(f"./data/{year}/{file}", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                stripped_row = [item.strip() for item in row]
                date_split = stripped_row[cols_1["date"]].split("/")
                print(date_split)
                d = datetime.datetime(date_split[2],date_split[0],date_split[1])
                d_before = datetime.datetime(2014, 6, 1)
                if :
                    print("bef")
                    pass
                else:
                    print("aft")
                    pass
