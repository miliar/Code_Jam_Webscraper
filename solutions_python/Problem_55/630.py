fin = file("C-small-attempt0.in","r")

ls = [e.strip() for e in fin.readlines()]

T = int(ls.pop(0))
#print T
for case in xrange(T):
    l_1 = ls.pop(0).split()
    r,k,n = int(l_1[0]), int(l_1[1]), int(l_1[2])
    l_2 = ls.pop(0).split()
    ar = []
    for e in l_2:
        ar.append(int(e))
    
    #print r,k
    #print ar
    #print

    pos = 0
    euro = 0
    for run in xrange(r):
        left = 0 + k
        max_roll = 0 + n
        while ( (ar[pos] <= left) and (max_roll>0) ):
            lawl = ar[pos]
            euro+=lawl
            left-=lawl
            max_roll-=1
            pos+=1
            if (pos==n):
                pos = 0
    print "Case #"+str(case+1)+": "+str(euro)
        
