import sys

def calc(P, K, freq):
    if P*K<len(freq):
        return None
    
    c=0
    keys=[P for x in range(K)]
    while len(freq)>0:
        m=max(freq)
        n=max(keys)
        ni=keys.index(n)
        c+=(P-n+1)*m
        keys[ni]-=1
#        print m,(P-n+1),keys

        freq.remove(m)
        
    return c

def go(name):
    f=file(name)

    line=f.readline().strip()
    total=int(line)
    for i in range(total):
        P,K,L=[int(x) for x in f.readline().strip().split()]
        freq=[int(x) for x in f.readline().strip().split()]
        freq=freq[:L]
        r=calc(P,K, freq)
        
        if r!=None:
            print "Case #%d: %d" %(i+1, r)
        else:
            print "Case #%d: impossible" % (i+1)
    f.close()

            
try:
    fn=sys.argv[1]
except:
    print "Usage:\n", "python", sys.argv[0]+" input_file_name"
    sys.exit(1)

go(fn)
