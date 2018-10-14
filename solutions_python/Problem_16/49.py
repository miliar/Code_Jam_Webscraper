from time import time
import psyco
import re
import math
psyco.full()

fin = open("c4_input.txt","r")
fout = open("c4_output.txt","w")
cases = int(fin.readline())

def runlength(s):
    current = s[0]
    groups = 1
    for l in s:
        if l != current:
            current = l
            groups += 1
    return groups

def permute(s, seq, k):
    shift = 0
    current = ""
    groups = 0
    count = -1
    for posi in range(len(s)):
        count += 1
        if count == k:
            shift += k
            count = 0
        #print "shift:",shift, count
        nextletter = s[shift+seq[count]]
        #print nextletter
        if nextletter != current:
            current = nextletter
            groups += 1
    return groups

        
    
def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            #print k, part  # test
            for m in permutate(part):
                temp.append(seq[k:k+1] + m)
                #print m, seq[k:k+1], temp  # test
        return temp

t0 = time()
for casenr in range(cases):
    k = int(fin.readline())
    s = fin.readline()[:-1]
    minlength = runlength(s)
    minmutes = 10000000
    for p in permutate(range(k)):
        minmutes = min(minmutes, permute(s, p, k))
    


    print "Time elapsed: %f" % (time() - t0)
    fout.write("Case #%d: %d\n" % (casenr+1, minmutes))
    