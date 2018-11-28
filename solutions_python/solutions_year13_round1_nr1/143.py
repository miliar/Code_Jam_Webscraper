import math
from math import *

def getkapprox(r,t):
    r = int(r)
    t = int(t)
    k = floor(sqrt(t/2. + ((2*r-1)**2)/16.) - (2*r-1)/4.)
    return k

def getpaint(k,r):
    k = int(k)
    r = int(r)
    return (2L*k)*k + k*(2L*r-1L)

def getk(r,t):
    #k = int(getkapprox(r,t))
    #bot = int(floor(k/2))
    #top = k*2+1
    #if bot<0:
    #    bot = 0
    bot = 1
    top = t
    
    if getpaint(bot,r)>t:
        print "ERROR", bot, top
    if getpaint(top,r)<t:
        print "ERROR", bot, top
    while bot < top:
        med = (bot+top+1)/2
        if getpaint(med,r)>t:
            top = med-1
        else:
            bot = med
    return bot

fo = open("circle.out","w")

f = open("A-large.in","r")
T = int(f.readline().strip())
test = 1
while test <= T:
    if test%100 == 0:
        print test
    data = f.readline().strip().split()
    r = long(data[0])
    t = long(data[1])
    #print r,t
    fo.write("Case #%d: %d\n" % (test, getk(r,t)))
    test = test+1
    
fo.close()
f.close()
