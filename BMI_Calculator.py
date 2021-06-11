import json
from collections import defaultdict

data_file = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]

# dict_data = json.loads(data_file)
# print(type(dict_data))

# res = defaultdict(list)
# for sub in data_file:
#     for key in sub:
#         res[key].append(sub[key])
#         print(key['HeightCm'])
#
#
# # printing result
# print("The extracted dictionary : " + str(dict(res)))


def Calc_BMI(mass, height):
    BMI = mass / (height ** 2)
    if BMI >= 18.4 and BMI <= 24.5:
        print("Underweight")
    elif BMI >= 25 and BMI <= 29.9:
        print("Normal Weight")
    elif BMI >= 30 and BMI <= 34.9:
        print("Overweight")
    elif BMI >= 35 and BMI <= 39.9:
        print("Moderately obese")
    elif BMI >= 40:
        print("Severely obese")


for data in data_file:
    height = data['HeightCm']
    mass = data['WeightKg']
    Calc_BMI(mass, height)
