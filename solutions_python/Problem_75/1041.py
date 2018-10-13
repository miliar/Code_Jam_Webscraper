#!/usr/bin/env python

# Getting file descriptors

f = open('input-1.in', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')


# Defining functions

def is_opposed(k, q, l):
    if l in k.keys():
        if k[l] in q:
            return 1
        else:
            return 0
    else:
        return 0
        
def forms_combo(k, q, l, m):
    if l+m in k.keys():
        return 1
    else:
        return 0

def process(lne):
    i = lne.split()
    C = int(i[0])
    D = int(i[C+1])
    N = int(i[-2])
    subkey = {}
    rmkey = {}
    ellist = []
    Flag = 0
    
    for k in range(1,C+1,1):
        subkey[i[k][0]+i[k][1]]=i[k][-1]
        subkey[i[k][1]+i[k][0]]=i[k][-1]
    
    for m in range(1,D+1,1):
        rmkey[i[C+m+1][0]]=i[C+m+1][1]
        rmkey[i[C+m+1][1]]=i[C+m+1][0]
    
    WS = i[-1]
    
    for n in WS:
        ellist.append(n)
        if len(ellist) > 1:
            if forms_combo(subkey, ellist, n, ellist[-2]):
                z = ellist[-2]
                del ellist[-2]
                del ellist[-1]
                ellist.append(subkey[n+z])
            elif is_opposed(rmkey, ellist, n):
                ellist = []
    Result = ""
    for e in ellist:
        Result = Result + str(e) + ", "
    Result = Result[0:-2]
    return "["+Result+"]"        

# Getting input and processing

LineNum = 0

for line in f:
    if LineNum == 0:
        NumCases = int(line)
        LineNum += 1
    else:
        s.write("Case #%d: %s\n"%(LineNum,process(line)))
        LineNum += 1




# Closing files

f.close()
s.close()