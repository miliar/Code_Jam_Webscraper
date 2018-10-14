from math import *

def func(d,n,l):
    max_time = 0
    for horse in l:
        time = (d-horse[0])/horse[1]
        if time > max_time:
            max_time = time
    return d/max_time

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d,n = [int(s) for s in input().split()]
    l = []
    for j in range(n):       
        l.append([int(s) for s in input().split()])
    print("Case #{}: {}".format(i, func(d,n,l)))
