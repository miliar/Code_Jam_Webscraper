#!/bin/python
i = open('C-small-attempt0.in')
o = open('code.out','w')

def restr(z,s):
    for n in xrange(len(z)):
        if z[-n]=="0":
            continue
        if z[-n:]+z[:-n] == s:
            #print z[-n:]+z[:-n], z, s
            return True
    return False

def is_recyclable(ino,b):
    count = 0
    s = str(ino)
    for z in xrange(ino+9,b+1):#max((10^len(s)+1)-1,b+1)):
        zs = str(z)
        if restr(zs,s):
            count +=1
    return count

for t in xrange(int(i.readline())):
    a,b = [int(x) for x in i.readline().split(' ')]
    skip = []
    count = 0
    for ino in xrange(a,b+1):
        count+= is_recyclable(ino,b)
    o.write("Case #%d: %d"%(t+1, count)+"\n")
    print "Case #%d: %d"%(t+1, count)

i.close()
o.close()