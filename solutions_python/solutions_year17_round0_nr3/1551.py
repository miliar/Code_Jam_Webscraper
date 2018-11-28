#!/usr/bin/python3

def isEven(x):
    return not(x & 1)

def isOdd(x):
    return x & 1

def func(val, i):
    people = i - 1
    large = int(val // 2)
    small = large
    
    if (isEven(val)):
        small -= 1
        
    a = (people // 2);
    if isOdd(people):
        a += 1
        
    next = large if isOdd(people) else small
   
    if(i > 1):
        return func(next, a)
    else:  
        return large, small
    
    


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):   
    s, p = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    
    large, small = func(s, p)


    print("Case #{}: {} {}".format(i, large, small))
    # check out .format's specification for more formatting options
