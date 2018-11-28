
sp = lambda x,y: x + y


ifile = open("C:\Python25\source\C-small-attempt0.in")
ofile = open("gcj2010-q-3-small.txt", 'w')

cases = int(ifile.readline().split()[0])

for c in range(1, cases+1):
    line = ifile.readline()
    R, k, N = tuple(map(int,line.split()))
    q_group = map(int, ifile.readline().split())
    euro = 0
    for r in range(R):
        pre_passengers = 0
        for i in range(1, N+1):
            passengers = reduce(sp, q_group[:i])
            if passengers == k:
                euro += k
                q_group = q_group[i:] + q_group[:i]
                break
            elif passengers > k:
                euro += pre_passengers
                q_group = q_group[i-1:] + q_group[:i-1]
                break
            elif passengers < k and i == N:
                euro += passengers
            pre_passengers = passengers
    ofile.write("Case #%d: %d\n" % (c, euro))
                
            
            
            
        
