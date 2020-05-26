# Basic numbers
base_salary = 1200
base_salary_per_hour = 7.191
weekend_job_bonus = 0.2
night_shift_bonus = 0.50
holiday_shift_bonus = 1
holiday_shift_night_bonus = 1.5
work_bonus = 0.10
overtime_Cash = 14.44
social_tax = 0.11
salary_tax = 0.20
night_shift_hours = 6.5
night_shift_hours_week = 1.5
one_bonus_hour = 1
night_one_hour = 5.5
basic_hours = 8

bs_hour_check = input("Месяц целиком отработал? - Yes / No")

daycounter = None
base_Salary_Less = None

if bs_hour_check == "Yes":
    base_salary = 1200
elif bs_hour_check == "No":
    month = int(input("Введи текущий месяц в формате 1/2/3..."))
    if month == 1 or month == 3 or month == 9 or month == 10:
        daycounter = 22
    elif month == 2 or month == 4 or month == 6 or month == 11 or month == 12:
        daycounter = 20
    elif month == 5:
        daycounter = 19
    elif month == 7:
        daycounter = 23
    elif month == 8:
        daycounter = 21
    days = int(input("Введи количество отработанных дней"))
    base_Salary_Less = 1200 / daycounter * days
else:
    print("Ты что-то сделал не так, начни заного")

year_bonus = input("Ты год в компании работаешь? Yes/No")
if year_bonus == "Yes" and bs_hour_check == "Yes":
    base_salary = base_salary + (base_salary * work_bonus)
    print("Бонус полного месяца активирован")
elif year_bonus == "Yes" and bs_hour_check != "Yes":
    base_salary = base_Salary_Less + (base_salary * work_bonus)
    print("Бонус с учётом не полного месяца активирован")
else:
    print("Бонус не активирован")

# Подсчёт ночных смен + обычное утро (пн-пт)
night_Shifts = int(input("Ночная смена?"))
if year_bonus == "Yes":
    night_Shift_Payment = ((base_salary_per_hour * night_shift_bonus * night_Shifts) +
                           (night_Shifts * base_salary_per_hour * night_shift_bonus * work_bonus)) * night_shift_hours
else:
    night_Shift_Payment = base_salary_per_hour * night_shift_bonus * night_Shifts * night_shift_hours

# Подсчёт ночных смен с переходом на выходной день после 06:00 (сб-вс)
night_Shift_Weekend = int(input("Обычная ночная смена + выходное утро?"))
if year_bonus == "Yes":
    night_Shift_Bonus_Weekend = (((base_salary_per_hour * weekend_job_bonus * night_Shift_Weekend) +
                                  (night_Shift_Weekend * base_salary_per_hour * weekend_job_bonus * work_bonus))
                                 * night_shift_hours_week) + \
                                (((night_Shift_Weekend * base_salary_per_hour * night_shift_bonus) +
                                  (night_Shift_Weekend * base_salary_per_hour * night_shift_bonus * work_bonus))
                                 * night_shift_hours)
else:
    night_Shift_Bonus_Weekend = night_Shift_Weekend * night_shift_hours_week * base_salary_per_hour * \
                                weekend_job_bonus \
                                + (night_Shift_Weekend * base_salary_per_hour * night_shift_hours * night_shift_bonus)

# Подсчёт обычных выходных (сб-вс) смен

weekend_Shift = int(input("Выходные смены?"))
if year_bonus == "Yes":
    weekend_Shift_Calculation = ((weekend_Shift * base_salary_per_hour * weekend_job_bonus) +
                                 (weekend_Shift * base_salary_per_hour * weekend_job_bonus * work_bonus)) * basic_hours
else:
    weekend_Shift_Calculation = weekend_Shift * base_salary_per_hour * weekend_job_bonus * basic_hours

# Подсчёт обычных (пн-пт) праздничных смен
holiday_Shift = int(input("Праздничная дневная смена?"))
if year_bonus == "Yes":
    basic_Holiday_Shift = ((holiday_Shift * base_salary_per_hour * holiday_shift_bonus)
                           + (holiday_Shift * base_salary_per_hour * holiday_shift_bonus * work_bonus)) * basic_hours
else:
    basic_Holiday_Shift = holiday_Shift * base_salary_per_hour * holiday_shift_bonus * basic_hours

# Подсчёт праздничных ночных смен + обычное утро (пн-пт)
holiday_Night = int(input("Праздничная ночная смена + обычное утро?"))
if year_bonus == "Yes":
    holiday_Night_Shift = ((holiday_Night * base_salary_per_hour * holiday_shift_night_bonus) +
                           (holiday_Night * base_salary_per_hour * holiday_shift_night_bonus * work_bonus)) * \
                          night_shift_hours
else:
    holiday_Night_Shift = holiday_Night * base_salary_per_hour * night_shift_hours * holiday_shift_night_bonus

# Подсчёт праздничных ночных смен + праздничных дневных

holiday_Night_Weekend = int(input("Праздничная ночная + праздничное утро?"))
if year_bonus == "Yes":
    holiday_Night_Weekend_Shift = (((holiday_Night_Weekend * base_salary_per_hour * holiday_shift_night_bonus) +
                                    (holiday_Night_Weekend * base_salary_per_hour * holiday_shift_night_bonus *
                                     work_bonus)) *
                                   night_shift_hours) + (((holiday_Night_Weekend * base_salary_per_hour *
                                                           holiday_shift_bonus) + (holiday_Night_Weekend *
                                                                                   base_salary_per_hour *
                                                                                   holiday_shift_bonus * work_bonus))
                                                         * night_shift_hours_week)
else:
    holiday_Night_Weekend_Shift = ((holiday_Night_Weekend * base_salary_per_hour * holiday_shift_night_bonus)
                                   * night_shift_hours) + ((holiday_Night_Weekend * base_salary_per_hour *
                                                            holiday_shift_bonus) * night_shift_hours_week)

# Подсчёт праздничных ночных смен + выходной день

holiday_Niweekend = int(input("Праздничная ночная + обычный выходной?"))
if year_bonus == "Yes":
    holiday_niweekend_Shift = (((holiday_Niweekend * base_salary_per_hour * holiday_shift_night_bonus) +
                                (holiday_Niweekend * base_salary_per_hour * holiday_shift_night_bonus * work_bonus))
                               * night_shift_hours) \
                              + (((holiday_Niweekend * base_salary_per_hour * weekend_job_bonus) +
                                  (holiday_Niweekend * base_salary_per_hour * weekend_job_bonus * work_bonus))
                                 * night_shift_hours_week)
else:
    holiday_niweekend_Shift = ((holiday_Niweekend * base_salary_per_hour * holiday_shift_night_bonus) *
                               night_shift_hours) + ((holiday_Niweekend * base_salary_per_hour * weekend_job_bonus)
                                                     * night_shift_hours_week)

# 1 час красного дня + ночь + обычное утро

red_One_Night = int(input("1 час красной ночи + обычная ночь + обычное утро"))
if year_bonus == "Yes":
    red_One_Night_Shift = (((red_One_Night * base_salary_per_hour * holiday_shift_night_bonus) +
                            (red_One_Night * base_salary_per_hour * holiday_shift_night_bonus * work_bonus)) *
                           one_bonus_hour) + \
                          (((red_One_Night * base_salary_per_hour * night_shift_bonus) + (red_One_Night *
                                                                                          base_salary_per_hour *
                                                                                          night_shift_bonus *
                                                                                          work_bonus)) * night_one_hour)
else:
    red_One_Night_Shift = ((red_One_Night * base_salary_per_hour * holiday_shift_night_bonus) * one_bonus_hour) + \
                          ((red_One_Night * base_salary_per_hour * night_shift_bonus) * night_one_hour)
# 1 час красного дня + ночь + выходное утро

red_weekend = int(input("1 час красной ночи + обычная ночь + выходное утро"))
if year_bonus == "Yes":
    red_weekend_Shift = (((red_weekend * base_salary_per_hour * holiday_shift_night_bonus) +
                          (base_salary_per_hour * holiday_shift_night_bonus * work_bonus)) * one_bonus_hour) + \
                        (((red_weekend * base_salary_per_hour * night_shift_bonus) + (base_salary_per_hour *
                                                                                      night_shift_bonus *
                                                                                      work_bonus)) * night_one_hour) + \
                        (((red_weekend * base_salary_per_hour * weekend_job_bonus) +
                          (red_weekend * base_salary_per_hour * weekend_job_bonus * work_bonus))
                         * night_shift_hours_week)
else:
    red_weekend_Shift = ((red_weekend * base_salary_per_hour * holiday_shift_night_bonus) * one_bonus_hour) + \
                        ((red_weekend * base_salary_per_hour * night_shift_bonus) * night_one_hour) + \
                        ((red_weekend * base_salary_per_hour * weekend_job_bonus) * night_shift_hours_week)
# Овертаймы

overtime = int(input("Часы овертайма")) #overt
if year_bonus == "Yes":
    overtime_Hours = (overtime * overtime_Cash) + (overtime * overtime_Cash * work_bonus)
else:
    overtime_Hours = (overtime * overtime_Cash)

total_Cash = night_Shift_Payment + night_Shift_Bonus_Weekend + weekend_Shift_Calculation + basic_Holiday_Shift + \
             holiday_Night_Shift + holiday_Night_Weekend_Shift + holiday_niweekend_Shift + \
             red_One_Night_Shift + red_weekend_Shift + overtime_Hours + base_salary
total_Cash_After_Tax = (total_Cash - ((total_Cash * social_tax) +
                                      (total_Cash - (total_Cash * social_tax)) * salary_tax)).__round__(1)

print(f"Твоя зарплата до налогов: {total_Cash} Euro")
print(f"Твоя зарплата после налогов: {total_Cash_After_Tax} Euro")
