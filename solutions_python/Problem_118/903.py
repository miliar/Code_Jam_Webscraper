import math


fob = open("C-large-2.in")
#fob = open("C-large-1.in")

T = int(fob.readline())
f = fob.readlines()
fob.close()

import itertools

def possible(mesta):
    l = []
    if mesta==1:
        return ["1","2","3"]
    for x in map(''.join, itertools.product('01', repeat=mesta-2)):
        for i in ["0","1","2"]:
            l.append("1"+x+i)
    [l.append("2"+"0"*(mesta-2)+i) for i in ["0","1","2"]]
    return l

def palin():
    max_p = 50
    res = open("palin.in","w")
    res.write("1\n4\n9\n")
    for potenca in range(1,max_p+1):
        mesta = potenca/2 + 1
        print potenca
        
        if potenca%2==0:
            for i in possible(mesta):
                i_s = str(i)
                stevilo = int(i_s+i_s[-2::-1])
                i2 = str(stevilo**2)
                if i2==i2[::-1]:
                    res.write(i2+"\n")
        else:
            for i in possible(mesta):
                i_s = str(i)
                stevilo = int(i_s+i_s[::-1])
                i2 = str(stevilo**2)
                if i2==i2[::-1]: 
                    res.write(i2+"\n")     
    res.close()


hue = open("palin.in")
allez = hue.readlines()
hue.close()
res = open("res.out","w")
allez = [int(i) for i in allez]
for case in range(len(f)):
    [a,b] = f[case].split(' ')
    a = int(a)
    b = int(b)
    
    rez=len([i for i in range(len(allez)) if allez[i]>=a and allez[i]<=b])
    print case
    string = "Case #" + str(case+1) + ": " + str(rez) + "\n"
    res.write(string)

                
res.close()

'''
Created on 12. apr. 2013

@author: nraw
'''
