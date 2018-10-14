n = int(raw_input())
for i in range(1, n+1):
    t = [int(x) for x in raw_input().split()]
    total_dist = float(t[0])

    count = 0.0
    for j in range(t[1]):
        test = [int(x) for x in raw_input().split()]
        left = total_dist - test[0]    
        count = max(count, left/test[1])

    print "Case #" + str(i) + ": " + str(total_dist/count)
        
