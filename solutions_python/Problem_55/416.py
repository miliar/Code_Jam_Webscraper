# theme park

f = open('d:/jam/in3.txt')
T = int(f.next())

res = []

for cs in range(T):
    R,K,N = [int(x) for x in f.next().split(' ')] # 4,6,4
    q = [int(x) for x in f.next().split(' ')]

    #if cs!=1: continue

    if sum(q) <= K: # hame ja mishan!
        res.append( sum(q)*R )
        continue

    mon = 0
    for i in xrange(R):
        on = 0
        for ix, gi in enumerate(q):
            if (on+gi)>K:   # >= ?
                #print 'break@' + str(ix)
                break
            on += gi
        #
  
        q1 = q[:ix]
        q2 = q[ix:]
        mon += sum(q1)        
        q2.extend(q1)
        q = q2
        #print '%s -- %s  = %d' % (str(q1),str(q),mon)
        
        #break
    #
    res.append(mon)


#print res
f.close()

fw = open('d:/jam/ot3.txt', 'w')
for ix,r in enumerate(res):
    fw.write('Case #%d: %s\n' % (ix+1, r))
fw.close()



