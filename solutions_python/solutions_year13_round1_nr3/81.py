import sys

def check(k, p):
    for pp in p:
	if pp % k == 0:
	    return True
    return False

data = sys.stdin.readlines()
R, N, M, K = tuple(map(int, data[1].split()))
print "Case #1:"
for i in range(1, R+1):
    p = map(int, data[i+1].split())
    #print p
    d = [2, 2, 2]
    for k in range(3, 6):
	if check(k*k*k, p):
	    d = d + [k, k, k]
	elif check(k*k, p):
	    d = d + [k, k]
	elif check(k, p):
	    d = d + [k]
    d = sorted(d)
    d = d[::-1]
    #print d
    print "%d%d%d" % tuple(d[:3])
    
