# Даны длины сторон прямоугольного параллелепипеда.
# Найти его объем и площадь боковой поверхности.
a = int(input("Введите 1 сторону"))
b = int(input("Введите 2 сторону"))
c = int(input("Введите 3 сторону"))
v = a*b*c
s = 2*(a*b + b*c + a*c)
print(v)
print(s)
