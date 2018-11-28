#!/usr/bin/python
# Hermit - Code jam '10
# 05/08/'10 

f = open('large.in', 'r')
count = 0
for i in f.readlines():
    words = i.split()
    if(len(words) == 1): #First line, has to be the count
        total = words[0];
        continue;
    N = int(words[0]) #Claps
    K = int(words[1]) #Snappers
    count = count + 1
    if(((K+1)%pow(2,N)) == 0):
        output = "Case #"+str(count)+": ON"
    else:
        output = "Case #"+str(count)+": OFF"
    print output
