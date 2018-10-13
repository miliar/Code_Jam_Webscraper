import sys

line = sys.stdin.readline().strip()
N=int(line)
n=0

while n < N:
    n += 1
    line = sys.stdin.readline().strip()
    S = int(line)
    search = {}
    for s in range(S):
	name = sys.stdin.readline()[:-1]
	search[name] = s
    line = sys.stdin.readline().strip()
    Q = int(line)
    queries = []
    for q in range(Q):
	name = sys.stdin.readline()[:-1]
	queries.append(search[name])
    min_ch = Q+1
    # do it!
    last_seen = [-1] * S
    changes = 0
#    print S, Q, queries
    for i in range(Q):
        q = queries[i]
	last_seen[q] = i
#	print i, q, last_seen
	try:
	    last_seen.index(-1)
#	    print ########
	except ValueError:
	    # need change
#	    print "%s:%s" %(i, q)
	    changes += 1
	    for s in range(S):
	    	if last_seen[s] < i:
		    last_seen[s] = -1
	continue
    	
    print "Case #%s: %s" % (n, changes)

