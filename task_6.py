print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def divisor(a, b):
  if a == 0:
    print('Наибольший общий делитель:', b)
    exit()
  elif b == 0:
    print('Наибольший общий делитель:', a)
    exit()
  else:
    while a != 0 and b != 0:
      if a > b:
        a = a % b
      else:
        b = b % a
    print('Наибольший общий делитель:', a + b)

first_digit = int(input('Введите первое число: '))
second_digit = int(input('Введите второе число: '))
divisor(first_digit, second_digit)