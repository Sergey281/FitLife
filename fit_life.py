WATER_PER_KG = 30
CONVERSION_TO_ML = 1000
user_name = input("Как вас зовут?:")
user_age = int(input("Сколько вам полных лет:"))
user_weight = float(input("Сколько вы весите в кг (например, 75.6)?:"))
user_height = float(input("Какой у вас рост в метрах, (например 1.75)?:"))
bmi = user_weight / (user_height ** 2)  # индекс массы тела
water_needed = user_weight * WATER_PER_KG
water_1 = water_needed / CONVERSION_TO_ML

print(f"\nПривет, {user_name}!")
print(f"Ваш возраст: {user_age} лет(год)")
print(f"Ваш ИМТ: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_1:.3f} литра в день")
print("Расчет окончен. Будьте здоровы!")
