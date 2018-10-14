import sys

T = int(sys.stdin.readline().strip())

def rpi(n, w):
    result = 0
    
    return str(result)

for t in xrange(T):
    print 'Case #%d:' % (t + 1)
    N = int(sys.stdin.readline().strip())
    w = []
    for n in xrange(N):
	w.append(sys.stdin.readline().strip())
    wp = [0.0 for n in xrange(N)]
    for n in xrange(N):
	wp[n] = float(w[n].count('1')) / float(w[n].count('1') + w[n].count('0'))
	#print 'wp[%d]' % n, wp[n]
    owp = [0.0 for n in xrange(N)]
    for n in xrange(N):
	#calculate wp for other teams
	tp = 0.0
	for m in xrange(N):
	    if m == n:
		continue
	    if w[m][n] == '.':
		continue
	    wins = float(w[m].count('1'))
	    count = float(w[m].count('1') + w[m].count('0'))
	    count -= 1.0
	    if w[m][n] == '1':
		wins -= 1.0
	    owp[n] += wins / count
	    tp += 1.0
	owp[n] /= tp
	#print 'owp[%d]' % n, owp[n]
    oowp = [0.0 for n in xrange(N)]
    for n in xrange(N):
	tp = 0.0
	for m in xrange(N):
	    if m == n:
		continue
	    if w[m][n] == '.':
		continue
	    oowp[n] += owp[m]
	    tp += 1.0
	oowp[n] /= tp
	#print 'oowp[%d]' % n, oowp[n]
    for n in xrange(N):
	rpi = .25 * wp[n] + .5 * owp[n] + .25 * oowp[n]
	print rpi
