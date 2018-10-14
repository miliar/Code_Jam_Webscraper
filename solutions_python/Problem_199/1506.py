#!/usr/bin/python3

def flip(x):
    if(x == '-'):
        return '+'
    return '-'
    

t = int(input())  # read a line with a single integer
for line in range(1, t + 1):   
    n, m = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    pan = list(n)
    flipsize = int(m)
    res = 0;
    for i in range(len(pan)-(flipsize - 1)):
        if(pan[i] == '-'):
            for j in range(flipsize):
                pan[i+j] = flip(pan[i+j])
            res += 1    
    
    
    last = pan[len(pan) - (flipsize - 1) :]
    for k in last:
        if (k != '+'):
            res = "IMPOSSIBLE"
    
    print("Case #{}: {}".format(line, str(res)))
