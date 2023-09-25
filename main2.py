a = int(input())
b = int(input())
c = int(input())

largest = max(a, b, c)
smallest = min(a, b, c)
middle = a + b + c - smallest - largest

average = (largest + middle) / 2

print(int(average))




month_number = int(input())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= month_number <= 12:
    num_days = days_in_month[month_number - 1]
    print(num_days)
else:
    print("Invalid month number")


weight = int(input("Weight"))

if weight <= 60:
    category = "Lightweight"
elif 60 > weight <= 64:
    category = "First Welterweight"
elif 64 > weight <= 69:
    category = "Welterweight"
else:
    category = "Unknown"

# Print the determined weight category
print(category)


password = input()
confirm = input()

if password == confirm:
    print("Password accepted")
else:
    print("Password not accepted")


number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



num1 = int(input())
num2 = int(input())

if num1 < num2:
    smallest = num1
else:
    smallest = num2

print(smallest)




age = int(input())

if age <= 13:
    age_group = "childhood"
elif 14 <= age <= 24:
    age_group = "youth"
elif 25 <= age <= 59:
    age_group = "maturity"
else:
    age_group = "old age"

print(age_group)



angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == angle2 == angle3:
    triangle_type = "Equilateral"
elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Versatile"

print(triangle_type)





