# Даны целые числа , указывающие момент времени.
# Определить угол  между положением часовой стрелки в начале суток и в указанный момент времени.
(lambda hour, minute, second:
 print(abs(hour * 30 + minute * 0.5 + second * 0.5/60))) \
(float(input()), float(input()), float(input()))
