file = open("C-small.in")

T = int(file.readline())
for t in xrange(T):
    (R, k, N) = map(int, file.readline().split(" "))
    queue = map(int, file.readline().split(" "))
    
    money = 0
    #queue = []
    
    for r in xrange(R):
        rollercoster = []
        
        while len(queue) != 0:
            if sum(rollercoster) + queue[0] <= k:
                rollercoster.append(queue.pop(0))
            else:
                break
            
        money += sum(rollercoster)
        queue.extend(rollercoster)
    
    print "Case #%i: %i" % (t+1, money)