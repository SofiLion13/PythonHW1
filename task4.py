# Задача 4. Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Количество долек по горизонтали: "))
m = int(input("Количество долек по вертикали: "))
k = int(input("Сколько долек хотите отломить: "))

if k == n or k == m:
    print("YES")
elif k <= n*m:
    print("YES")
else:
    print("NO")
