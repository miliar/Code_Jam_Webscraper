import sys

data = sys.stdin.readline()

T = int(data.strip())

for t in range(0,T):
    data = sys.stdin.readline().strip().split(' ')
    
    R = int(data[0])
    k = int(data[1])
    N = int(data[2])
    
    g = sys.stdin.readline().strip().split(' ')
    
    g = map(lambda x: int(x), g)
    
    money = 0
    
    for i in range(0,R):
        
        space = k
        h = []
        
        while g and space >= g[0]:
           
            a = g.pop(0)
            space -= a
            money += a
            h.append(a)
            
        g += h
        
    print "Case #%d: %d" % (t + 1, money)
        
        
    
    