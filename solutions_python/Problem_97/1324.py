#!/usr/bin/env python


def bob(A, B):
    count = 0
    L = []
    for n in range(A,B):
        a = str(n)
        lst = map(int, a)
        lst2 = []
        lst2.extend(lst)
        #print "zob" + str(n)
        L2 = []
        for i in range(0,len(lst)-1):
            lst2.append(lst2.pop(0))
            zob = int(''.join(map(str,lst2)))
            if zob<=B and zob>n:
                L.append(zob* 10000+n)
                #print str(n) + " , " + str(zob)
                L2.append(zob)
        count+=len(set(L2))
    #L.sort()
    #if len(L) > 0:
    #    zob = L[0]
    #    for i in L[1:]:
    #        if zob==i:
    #            print i
    #        zob = i
        
    #print len(L)
    #print len(set(L))
    #print L
    return count
        #    tmpchr = a[i]
            
    


file = open("C-large.in")
index = 0
A = 0
B = 0
for line in file:
    if(index!=0):
        A = int(line.split()[0])
        B = int(line.split()[1])
        nb = bob(A,B)
        print "Case #" + str(index) + ": " + str(nb)
    index+=1



