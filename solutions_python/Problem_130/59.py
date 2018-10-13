T = input();
may = 0
for t in range(T):
    line = raw_input().split(' ')
    N = int(line[0])
    P = int(line[1])
    n0 = 0
    while(2**N-2**(N-n0)<P):
    	n0=n0+1
    must = 2**n0-2
    if(2**N==P):
    	must = 2**N-1
    n0 = 0
    while(2**(N-n0)>P):
    	n0=n0+1
    may = 2**N-2**n0

    print "Case #"+str(t+1)+":"+" "+str(must)+" "+str(may)
