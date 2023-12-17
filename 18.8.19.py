
sum = 0
tickets = (int(input("Введите количество билетов:")))
age = (int(input("Введите возраст посетителя:")))
for age in range(tickets):
     if age < 18:
        sum += 0
    elif  18<= age <= 25:
        sum += 990
    elif age > 25:
        sum += 1390
if tickets > 3:
    sum -= sum / 10
print("Стоимость Ваших билетов", sum)