
    
import sys
f = open(sys.argv[1], "rt")
T =  int(f.next().strip())
for t in range(T):
    N = int(f.next().strip())
    data = [map(int, f.next().strip().split()) for n in range(N)]
    count = sum((reduce(lambda x,y: x+(int(d[0]<y[0])^ int(d[1]<y[1])), data, 0) for d in data))/2
    print 'Case #%d: %d' %(t+1, count)

        
