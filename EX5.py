# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите значение X точки A: ')
xa = float(input())

print('Введите значение Y точки A: ')
ya = float(input())

print('Введите значение X точки B: ')
xb = float(input())

print('Введите значение Y точки B: ')
yb = float(input())

import math

ab = math.sqrt((xb-xa)**2+(yb-ya)**2)
print('Расстояние между точками = ', ab)