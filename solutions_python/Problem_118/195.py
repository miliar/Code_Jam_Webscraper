import sys, cPickle as pickle
from math import sqrt

#Note to anyone who reads this code:
#This code was run in two parts: Generating all the palindromes ahead of time
#and saving them to a file,
#Then reloading the entire list when running the real thing

fin = open("inp.in","r")
fout = open("out.txt","w")
T = int(fin.readline())

def getPals(limit):
    res = set()
    i=0
    while i<=9 and i<=limit:
        res.add(i)
        i+=1
    go = True
    i=1
    while go:
        binI = bin(i)[2:]
        rev = str(binI)[::-1]
        go = False
        for d in ["","0","1","2"]:
            n = int(str(binI) + d + rev)
            if n<=limit:
                go = True
                res.add(n)
        i+=1
    go=True
    i=0
    while go:
        go = False
        n = "2" + i*"0" + "2"
        if int(n)<=limit:
            go = True
            res.add(int(n))
        if len(n) % 2 == 1:
            n = "2" + ((i-1)/2)*"0" + "1" + ((i-1)/2)*"0" + "2"
            if int(n)<=limit:
                go = True
                res.add(int(n))
            n = "2" + ((i-1)/2)*"0" + "2" + ((i-1)/2)*"0" + "2"
            if int(n)<=limit:
                go = True
                res.add(int(n))
        i+=1
    return sorted(res)

#pals = getPals(sqrt(10**100))
#pickle.dump( pals, open( "pals.p", "wb" ) )
pals = pickle.load( open( "newpals.p", "rb" ) )
#newpals=[]

for trial in range(1,T+1):
    A,B = map(int,fin.readline().replace('\n','').split(' '))
    #A,B=1,10**100
    ans=0
    for n in pals:
        if n>=A and n<=B:
            ans+=1
        if n>B: break
    '''
        n=pal*pal
        if n>=A and n<=B:
            if str(n)==str(n)[::-1]:
                newpals.append(n)
                ans+=1
        if n>B: break
    '''
    fout.write( "Case #" + str(trial) + ": " + str(ans) + "\n")

fin.close()
fout.close()