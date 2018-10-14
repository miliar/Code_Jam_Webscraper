'''
Created on Sep 4, 2009

@author: indra
'''
import sys, os

filename = "C-large"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

WORD = "welcome to code jam"

N = int(reader.readline().rstrip())

caseno = 1
while caseno<=N:
    case = reader.readline().rstrip()
    l = len(case)
    dpar = [[0 for char in WORD] for letter in case]
    
    if case[0] == WORD[0]:
        dpar[0][0] = 1
    
    for ind in range(1,len(dpar)):
        dpar[ind][0] = dpar[ind-1][0]
        if case[ind] == WORD[0]:
            dpar[ind][0] += 1
        for sind in range(1,len(dpar[ind])):
            if case[ind] == WORD[sind]:
                dpar[ind][sind] = (dpar[ind-1][sind] + dpar[ind-1][sind-1]) % 10000
            else:
                dpar[ind][sind] = dpar[ind-1][sind]
    
    writer.write("Case #%s: %04d\n" % (str(caseno),dpar[-1][-1]))
    caseno+=1

writer.close()