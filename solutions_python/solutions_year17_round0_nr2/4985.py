#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:00:24 2017

@author: mohitgupta
"""
stack = []
temp = []
count = 1

f = open("B-small-attempt4.out.txt", 'w+')
f.close()


with open("B-small-attempt4.in.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
f.close()
n = int(content[0])
while(n > 0):
    num1 = int(content[count])

    while(num1 > 0):
        t = num1
        while(t > 0):
            stack.append(int(t%10))
            temp.append(int(t%10))
            t = int(t / 10)
        stack.sort(reverse = True)
        if (stack == temp):
            stack = []
            temp = []
            break
        else:
            num1 = num1 - 1
            stack = []
            temp = []
    f = open("B-small-attempt4.out.txt", 'a+')
    f.write("Case #" + str(count) + ": " + str(num1) + "\n")
    count += 1
