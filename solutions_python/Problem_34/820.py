#!/usr/bin/python
import re
file = open("A-large.in","r")
lines = file.readlines()
info = lines[0].split(" ")
D = int(info[0])
#print D
L = int(info[1])
#print L
N = int(info[2])
#print N

#print

salida = open("output.txt", "w")

for i in range(L+1,L+N+1):
    pattern = lines[i][:-1]
    pattern = re.sub(r"\(",r"[",pattern)
    pattern = re.sub(r"\)",r"]",pattern)
    pattern = "^%s$" % pattern
    count = 0
    #print lines[i],pattern
    for j in range(0,L+1):
        #print lines[j][:-1]
        if re.match(pattern,lines[j][:-1]):
             count = count + 1
    print "Case #%s: %s" % (i-L,count)
    print >> salida, "Case #%s: %s" % (i-L,count) 
        
         

