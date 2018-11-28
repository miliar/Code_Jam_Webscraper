T = int(input())
for t in range(1,T+1):
    max_time = 0
    d,n = [ int(i) for i in input().split() ]
    for i in range(n):
    	k,s = [ int(j) for j in input().split() ]
    	time = (d-k)*1.0/s
    	if time>max_time:
    		max_time = time
    else:
    	output = "Case #%d: %.6f"%(t,d/max_time)
    	print(output)
    