number = int(input("Число "))


digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

if digit1 + digit4 == digit2 - digit3:
    print("ДА")
else:
    print("НЕТ")


age = int(input("Возраст"))

if age >= 18:
    print("Access is allowed")
else:
    print("Access denied")




a = int(input())
b = int(input())
c = int(input())


if b - a == c - b:
    print("YES")
else:
    print("NO")




first = int(input("Первый"))
two = int(input("Два"))
three = int(input("Три"))
four = int(input("Четыре"))

if first == three and two == four:
    print("NO")
elif first == three or two == four:
    print("YES")
else:
    print("NO")


x = int(input("Раз"))
y = int(input("Два"))
z = int(input("Три"))
e = int(input("Четыре"))

if (x + 1) < z or (z + 1) < x or (y + 1) < e or (e + 1) < y:
    print("NO")
else:
    print("YES")




