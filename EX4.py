# Напишите программу, которая по заданному номеру четверти, ]
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите четверть (1/2/3/4)')
a = int(input())

if a == 1:
    print('Диапазон координат: x (0;∞), y (0;∞)')
elif a == 2:
    print('Диапазон координат: x (0;∞), y (-∞;0)')
elif a == 3:
    print('Диапазон координат: x ((-∞;0)), y (-∞;0)')
elif a == 4:
    print('Диапазон координат: x ((-∞;0)), y (0;∞)')
else:
    print ('Нет такой четверти')