print("Hello World")
name = ("ABCD")
age = 30

name = ("john")
age = 35

x = 2 + 3j
print(name)
print(x)

list = [1, 2, 3]
tuples = {1, 2, 3, 4}
sets = {2, 5, 7}
dictionary = {"name": "john"}

x = input("Enter your name:")
print(x)
print("Hello " + x)

e = input("Enter your birth year:")
c = int(e) + 2
print(c)

import keyword

print(keyword.kwlist)

x = input("Enter first number:")
y = input("Enter second number:")
sum = int(x) + int(y)
print(sum)

name = "MALATHY"
print(name.islower)
print(name.isupper)
print(name.find("a"))
print(name.replace("a", "e"))
print("T" in name)
print(5 + 2)
print(5 * 2)
print(5)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
a = 5
a += 4
print(2 == 5)
print(2 == 2)
print(2 != 5)

print(2 > 4 > 3)

i = 0
while i <= 10:
    print(i)
    i += 1

for i in range(10):
    print(i)

age = [10, 20, 28, 30, 45, 29]
print(age[1])
age.append(50)
age.insert(1, 24)
print(age)
print(len(age))
for age in age:
    if age > 30:
        print(age)

tuple = (10, 33, 45, 54, 45)
print(tuple.count(45))


def great():
    print("hello")
great()

