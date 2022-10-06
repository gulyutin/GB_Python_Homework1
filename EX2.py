# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значение X: ')
x = int(input())

print('Введите значение Y: ')
y = int(input())

print('Введите значение Z: ')
z = int(input())

left = not (x or y or z)
right = (not x and y and z)
if left == right:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")