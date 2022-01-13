Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello world")
hello world
num = 100
print(num)
100
print("Data Type of variable sum is", type(num))
Data Type of variable sum is <class 'int'>

fnum = 34.45
print(fnum)
34.45
print("Data Type of variable fnum is", type(fnum))
Data Type of variable fnum is <class 'float'>
cnum = 3 + 4j
print(cnum)
(3+4j)
print("Data Type of variable cnum is", type(cnum))
Data Type of variable cnum is <class 'complex'>

# Python program to print strings and type
str1 = "Hi my name is Oluwanifemi. I am a string"
str2 = 'Hi my name is Precious. I am also a string'
# Displaying string str1 and its type
print(str1)
Hi my name is Oluwanifemi. I am a string
print(type(str1))
<class 'str'>
# Displaying string str2 and its type
print(str2)
Hi my name is Precious. I am also a string
print(type(str2))
<class 'str'>
# Tuple
t1 = (1, 2, 3, 4, 5)
print(t1)
(1, 2, 3, 4, 5)
t2 = ("Nifemi", "Gina", "Marho")
for s in t2:
    print(s).
    
SyntaxError: invalid syntax
for s in t2:
    print(s)

    
Nifemi
Gina
Marho
t3 = (2, "Ebube", 45, "Jeffery")
'''
Print a specific element
indexes start with zero
'''
'\nPrint a specific element\nindexes start with zero\n'
print(t3[2])
45

# List of integers
lis1 = [1, 2, 3, 4, 5]
print(lis1)
[1, 2, 3, 4, 5]
lis2 = ["Mouse", "Keyboard", "Monitor"]
for x in lis2:
    print (x)

    
Mouse
Keyboard
Monitor
lis3 = [20, "CSC101", 15, "Python Programming"]
'''Print a specific element in list indexes start with zero'''
'Print a specific element in list indexes start with zero'
print("element at index 3 is:",lis3[3])
element at index 3 is: Python Programming

# Dictionary example
dict = {1:"Maryam","lastname":"Shefiu", "age":25}
print(dict[1])
Maryam
print(dict["lastname"])
Shefiu
print(dict["age"])
25

# Set Example
myset = {"Joseph", "Adaobi", "Kamara", "Ugochi"}
for a in myset:
    print(a)

    
Adaobi
Ugochi
Kamara
Joseph
print(2 in myset)
False
myset.add(99)
print(myset)
{'Ugochi', 99, 'Joseph', 'Kamara', 'Adaobi'}

# Programming Simple interest problem
p = 1000
r = 1
t = 2
A = (p * ( 1 + ((r / 100.0) * t)))
print("Amount is", A)
Amount is 1020.0
SI = A - p
print("Simple Interest is", SI)
Simple Interest is 20.0

# Solve the quadratic equation ax**2 + bx + c = 0
import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('the solution are', sol1, sol2)
the solution are (-3+0j) (-2+0j)

# Program to find the area of a triangle
a = float(input('Enter first side: '))
Enter first side: 5
b = float(input('Enter second side: '))
Enter second side: 6
c = float(input('Entet third side: '))
Entet third side: 7
s = (a+b+c) / 2
area = (s*(s-a)*(s-b)*(s-c)) **0.5
print('The area of the triangle is %0.2f' %area)
The area of the triangle is 14.70
