#!/usr/bin/env python

def palindromes(x):
    length = len(x)
    s = 1
    for i in range(0,length):
        if(x[i]!=x[-i-1]):
            s = 0
            break
    return s

def square(x):
    if round(x) == x:
        return 1
    return 0

def get_pal(x,y):
    total = 0
    while x<=y:
        if palindromes(str(x)):
            tmp = x**0.5
            if square(tmp):
                if palindromes(str(int(tmp))):
                    total = total + 1
        x = x + 1
    return total

file = open("C-small-attempt3.in",'r')
time = int(file.readline())
while time>0:
    t = time
    while time>0 :
        [x,y] = file.readline().split(" ")
        print("Case #{}: {}".format(t - time + 1, get_pal(int(x),int(y))))
        time = time - 1
