#!/usr/bin/python
import re

#Read input
f       = open('inp.txt', 'r')
lines   = f.readlines()
f.close()

#Output
f       = open('out.txt', 'w')
total   = lines.pop(0)
case_no = 0

def findfraction (x, gcdtoo=False, maxno=100):
    #remember x is exact
    win  = x
    deno = 100    

    if x == 0:
        return [0,maxno]
    
    if gcdtoo:
        common = gcd(win,deno)
        return [win/common,deno/common]
    else:
        return [win,deno]
    

def gcd(num1, num2):
    result = 1
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

def devable(a, b):
    return ((a%b == 0) or (b%a) == 0)

def goodanswer(x, listn, L, H):

    for each in listn:
        if (each < L ) or (each < H) or (not devable(x, int(each))):
            return False
            break
    return True

while(True):
    #Leave this out {
    if len(lines) == 0:
        break
    result = ""
    #}

    listn = lines.pop(0)    #case
    listn = listn.split(" ")

    N = int(listn[0])
    L = int(listn[1])
    H = int(listn[2])
    
    listn = lines.pop(0)    
    listn = listn.split(" ")


    #eliminate wrong input
    i = L
    result = "NO"
    while i <= H:
        if goodanswer(i, listn, L, H):
            result = i
            break
        i += 1
                 

    case_no   += 1
    output = "Case #"+str(case_no)+": "+str(result)
    print output
    output += "\n"
    #break
    f.write(output)
f.close()
