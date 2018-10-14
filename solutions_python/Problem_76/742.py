#! /usr/bin/env python3.0

import itertools as itrtls

def pat_sum(*li, bi=0): # patrick's sum
    if (len(li) == 0):
        return 0
    if ((li[0].__class__ == "".__class__) or (bi == 1)):
        return int(str(li[0]), 2)^pat_sum(*li[1:], bi=1)
    return li[0]^pat_sum(*li[1:])


def ok(sean, patrick): # ok for sean
    if (sum(sean) < sum(patrick)):
        return False
    return (pat_sum(*sean) == pat_sum(*patrick))

def complement(li, co):
    lis = li[:]
    
    for c in co:
        try:
            lis.remove(c)
        except:
            z = 1 # do nothing
    return lis

def force(li):
    maxim = 0
    for i in range(1, len(li)//2+1):
        combs = [list(l) for l in itrtls.combinations(li, i)]
        for comb in combs:
            compl = complement(li, comb)
            if (pat_sum(*comb) == pat_sum(*compl)):
                tmp = max([sum(comb), sum(compl)])
                maxim = tmp if (tmp > maxim) else maxim
    
    return maxim

fic = input()

f = open(fic, "r")
lines = [li.replace("\n", "") for li in f.readlines()][1:][1::2]
f.close()

f = open("output.txt", "w")

for i in range(len(lines)):
    
    line = [int(n) for n in lines[i].split(" ")]
    
    if (not pat_sum(*line) == 0):
        result = "NO"
    
    elif (len(line) == 2):
        result = max(line)
    else:
        result = force(line)
    out = "Case #"+str(i+1)+": "+str(result)
    print(out)
    f.write(out+"\n")

f.close()