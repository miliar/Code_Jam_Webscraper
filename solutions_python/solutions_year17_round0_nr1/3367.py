#!/usr/bin/env python3

def flip(curstr,i,k):
    newstr = []
    for ctr in range(k):
        if curstr[i+ctr] == '+':
            newstr.append('-')
        else:
            newstr.append('+')

    return curstr[:i]+"".join(newstr)+curstr[i+k:]
#with open('test.txt') as infile:
t = int(input())
#print(t)
for casenum in range(t):
    line = input()
    start,k = line.split()
    k = int(k)
    length = len(start)-k+1
    
    end = '+'*len(start)
    strs = {end:0}
    cur_strs = [end]

    found = False
    while(len(cur_strs)>0):
        new_strs = []
        for curstr in cur_strs:
            for i in range(length):
                newstr = flip(curstr,i,k)
                if newstr not in strs:
                    strs[newstr] = strs[curstr]+1
                    new_strs.append(newstr)

        if start in strs:
            print("Case #{}: {}".format(casenum+1,strs[start]))
            new_strs = []
            found = True

        cur_strs = new_strs

    if not found:
        print("Case #{}: {}".format(casenum+1,"IMPOSSIBLE"))

