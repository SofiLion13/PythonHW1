# Задача 3. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 - счастливый, т.к. 3+8+5=9+1+6. 

happy = int(input("Введите номер билетика: "))
a1 = happy // 100000
a2 = happy // 10000 % 10
a3 = happy // 1000 % 10
a4 = happy // 100 % 10
a5 = happy // 10 % 10
a6 = happy % 10
if a1 + a2 + a3 == a4 + a5 + a6:
    print("YES")
else:
    print("NO")