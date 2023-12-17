#!/usr/bin/python3
n = int(input("Input number of lines:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        i += 1
        print(j, end=" ")
    print()