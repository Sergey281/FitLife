user_name = input("Как вас зову?: ") 
user_age = int(input("Сколько вам полных лет: ")) 
user_weight = float(input("Сколько вы весите (в кг)?: ")) 
user_height = float(input("Какой у вас рост (в метрах, например 1.75)?: ")) 
bmi = user_weight / (user_height ** 2) # индекс массы тела
water_needed = user_weight * 30 # 30 это станд. реком.
water_1 = water_needed / 1000

print(f"\nПривет, {user_name}!")
print(f"Ваш возраст: {user_age} лет(год)")
print(f"Ваш ИМТ: {bmi:.0f}")
print(f"Рекомендуемая норма воды: {water_1:.3f} мл в день")
print("Расчет окончен. Будьте здоровы!")
print()

