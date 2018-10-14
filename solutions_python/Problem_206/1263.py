
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    d, n = [int(p) for p in raw_input().split(" ")]  # read a list of integers, 2 in this case
    mosttime = 0
    
    for j in range(n):
        k, s = [int(m) for m in raw_input().split(" ")]  # read a list of integers, 2 in this case
        
        mosttime = max((d-k)/ float(s) ,mosttime ) 
        
    print "Case #{}: {} ".format(i,d/float(mosttime))