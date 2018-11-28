from math import log


def gcd(a,b):
    r = a%b                 # step 1
    if r == 0:              # step 2
	return b
    else:
	return gcd(b,r)     # step 3

def checkElf(P, Q):
    g = gcd(P,Q)
    P /= g
    Q /= g
    l = log(Q, 2)
    if not l.is_integer():
	return -1
    while P != 1:
	if P == -1:
	    return 'fuck'
	P -= 1
        Q /= 2
        if P == 2:
	    P = 1
	    break
        P /= 2
	g = gcd(P,Q)
	P /= g
	Q /= g
    return int(log(Q, 2))


f = open('A-small-attempt0.in', 'r')
fw = open('output.out', 'w')
r = f.readline()
for i in range(int(r)):
    r = f.readline()
    s = r.replace('\n', '').split('/')
    e = checkElf(int(s[0]), int(s[1]))
    if e == -1:
	e = "impossible"
    fw.write('Case #' + str(i+1) + ': ' + str(e) + '\n')
 
    
