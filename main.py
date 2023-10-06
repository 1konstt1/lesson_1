print("Система расчёта штрафов d Германии")

car_speed = 147
is_town = True

fine_for_town_1_to_10 = 30
fine_for_town_11_to_15 = 50
fine_for_town_16_to_20 = 70
fine_for_town_21_to_25 = 115
fine_for_town_26_to_30 = 180
fine_for_town_31_to_40 = 260
fine_for_town_41_to_50 = 400
fine_for_town_51_to_60 = 560
fine_for_town_61_to_70 = 700
fine_for_town_70_and_more = 800

fine_for_country_1_to_10 = 20
fine_for_country_11_to_15 = 40
fine_for_country_16_to_20 = 60
fine_for_country_21_to_25 = 100
fine_for_country_26_to_30 = 150
fine_for_country_31_to_40 = 200
fine_for_country_41_to_50 = 320
fine_for_country_51_to_60 = 480
fine_for_country_61_to_70 = 600
fine_for_country_70_and_more = 700


town_speed = 50
country_speed = 70

if is_town:
  over_speed = car_speed - town_speed
else:
  over_speed = car_speed - country_speed

if over_speed < 1:
  print("Скорость не превышена или превышена незначительно")
elif over_speed >= 1 and over_speed <= 10:
  print("Штраф: " + str(fine_for_town_1_to_10) )
  