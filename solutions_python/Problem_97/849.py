#!/usr/bin/env python

f = open("c.in", "r")
fout = open("c.out", "w")

data = f.readlines()

#print data
#print int(data[0])

def is_recycled(sn, sm):


    return False

for i in range (1, int(data[0])+1):
    l = data[i].rstrip('\n')
#    print l
    s = l.split(" ")

    a = int(s[0])
    b = int(s[1])
    nb = 0 # result

    for n in range(a, b+1):
        sn = str(n)
        ln = len(str(n))
        tn = ''.join(sorted(sn))
        
        for m in range(n+1, b+1):
            #if m >= n*10: next
            #print n,m
            sm = str(m)

            tm = ''.join(sorted(sm))
            if tn != tm: continue

            lm = len(sm)
            #if ln != lm: continue

            for k in range(1,ln):
                li = lm-k
                #print sn[:i],sm[len(sm)-i:]
                #print sn[i:],sm[:len(sm)-i]
                if sn[:k] == sm[li:] and sn[k:] == sm[:li]:
                    #print "->", n, m
                    nb += 1
                    break

            #n = 12345
            #m = 34512

            #for k in range(1,ln):
                #if 10**i > n: continue
                #print n, n/10**i, (n-n/10**i*10**i), m, m/10**(ln-i), (m-m/10**(ln-i)*10**(ln-i))
                #if (n-n/10**k*10**k)*10**(ln-k+1) + n/10**k == m:
                #    print n, m, (n-n/10**i*10**i)*10**(ln-i+1) + n/10**i
                #    nb += 1
                #    break
                

#    print s
    res = "Case #{0}: {1}\n".format(i, nb)
    print res.rstrip()
    fout.write(res)

