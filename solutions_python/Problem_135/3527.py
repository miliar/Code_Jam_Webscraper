#!/bin/python
# -*- coding: utf-8 -*

ERROR = "Volunteer cheated!"
BAD = "Bad magician!"
SIZE = 4

grid1 = {}
grid2 = {}
ans1 = -1
ans2 = -1

f = open("input.txt", 'r')
f2 = open("output.txt", 'w')
t = int(f.readline())
n = 1
while t:
    s1 = set()
    ans1 = int(f.readline())
    for l in range(SIZE):
        if l+1 == ans1 :
            for x in f.readline().split() :
                s1.add(x)
        else :
            f.readline()
        
    s2 = set()
    ans2 = int(f.readline())
    for l in range(SIZE):
        if l+1 == ans2 :
            for x in f.readline().split() :
                s2.add(x)
        else :
            f.readline()
    
    
    i = s1.intersection(s2)
    print(s1)
    print(s2)
    print(i )
    isize = len(i)
    if isize == 1 :
        f2.write("Case #{}: {}\n".format(n, i.pop()))
    elif isize == 0 :
        f2.write("Case #{}: {}\n".format(n, ERROR))
    else :
        f2.write("Case #{}: {}\n".format(n, BAD))

      
    n += 1
    t -= 1
    
f.close()
f2.close()

