
zad = open("A-large.in").read()
z = zad.split('\n')

o = open("out.txt",'w')

try:
    for l in xrange(1,len(z)):

        NK = z[l].split()
        N = int(NK[0])
        K = int(NK[1])
    
        K= K%2**N
        
                   
        if K==2**N-1:
            #print "Case #%d: ON" % l
            o.write("Case #%d: ON\n" % l)
        else:
            #print "Case #%d: OFF" % l
            o.write("Case #%d: OFF\n" % l)
except:
    print "nana"
        
print "ok"
