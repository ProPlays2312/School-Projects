#!/usr/bin/python3
def add():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a+b)
def sub():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a-b)
def mul():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a*b)
def div():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a/b)
def fldiv():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a//b)
def exp():
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print("Answer is", a**b)
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Floor Divition \n6. Exponent")
x = int(input("Select your operation 1-6:"))
if x == 1:
    add()
if x == 2:
    sub()
if x == 3:
    mul()
if x == 4:
    div()
if x == 5:
    fldiv()
if x == 6:
    exp()