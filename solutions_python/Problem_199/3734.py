import sys
sys.setrecursionlimit(10000)

class Impossible(Exception):
    pass



def iterate(n, s, k):
    assert n >= k, "String should be bigger than k."
    
    if n == k:        
        if s == 2**n - 1:
            return 0        
        elif s == 0:            
            return 1        
        raise Impossible
    
    if s  % 2 == 1:        
        return iterate(n -1, s >> 1, k)
    return 1 + iterate(n - 1, (s ^ (2**k - 1)) >> 1, k)    
    


fd = open(sys.argv[1])
data = fd.read().split("\n")

n = int(data[0])

for i in range(n):
    s, k = data[1 + i].split(" ")
    n = len(s)
    k = int(k)    
    s = int(s.replace("+","1").replace("-", "0"), 2)
    try:
        print "case #%d: %d" % (i +1, iterate(n, s, k))        
    except Impossible:
        print "case #%d: IMPOSSIBLE" % (i + 1, )


#print iterate(6, 0b110000, 2)



