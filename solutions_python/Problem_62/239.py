

tests = int(raw_input())

for g in xrange(tests):
    n_wires = int(raw_input())
    wires_left = []
    for w in xrange(n_wires): 
        tmp = map(int,raw_input().split())
        wires_left.append((tmp[0],tmp[1]))
    wires_left.sort()
    
    counter = 0 
    for x in xrange(n_wires):
        current = wires_left[x]
        for t in xrange(n_wires-x):
            target = wires_left[t+x]
            if (current[0]<target[0] and current[1]>target[1]):
                counter = counter + 1
            elif (current[0]>target[0] and current[1]<target[1]):
                counter = counter+1
                
                
    print "Case #%d:"%(g+1),counter
    