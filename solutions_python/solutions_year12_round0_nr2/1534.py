import sys
output = "Case #%s: %s"
f = open(sys.argv[1],'r')
T = int(f.readline())
for counter in xrange(T):
    line  = [int(i) for i in f.readline().strip().split(' ')]
    N = line[0]
    S = line[1]
    p = line[2]
    t = line[3:]

    #print N
    #print S
    #print p
    #print t

    # calculus
    normal = p*3-2 if p*3-2 >0 else 0
    surprise = normal - 2 if normal-2>0 else 0
    if p ==1:
        surprise = 1
    t.sort()
    #print t
    toadd = 0
    counter2 = -1
    sol = 0
    #import pdb; pdb.set_trace()
    for i in t:
        counter2 +=1
        if S>0:
            if i<surprise:  
                continue
            else:
                S-=1
                toadd+=1
                continue

        else:
            if i < normal:
                continue
            else:
                sol = len(t) - counter2 
                break
    sol += toadd
    print output % (counter+1, sol)
