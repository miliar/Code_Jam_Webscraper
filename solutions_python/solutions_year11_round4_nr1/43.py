import sys

T=int(sys.stdin.readline())

def dodo(ll, R, S, t):
#	print ll, R, S, t
	run = min(t, float(ll)/R)
#	print run
	return (t-run, float(R*run - S*run)/S)

for case in range(T):
	print "Case #%d:" % (case+1),
	X, S, R, t, N = map(int, sys.stdin.readline().split(' '))
	B = [0]*N
	E = [0]*N
	w = [0]*N
	for i in range(N):
		(B[i], E[i], w[i]) = map(int, sys.stdin.readline().split(' '))
	
	p = 0
	noskip = float(X)
	unsaved = 0
	for i in range(N):
		noskip -= (E[i] - B[i])
		unsaved += float(E[i] - B[i]) / (S+w[i])

	unsaved += float(noskip) / S

	t, saved = dodo(noskip, R, S, t)
	sw = sorted(enumerate(w), key=lambda x: x[1])
#	print sw
	for idx, _ in sw:
		t, save = dodo(float(E[idx]-B[idx]), R+w[idx], S+w[idx], t)
#		print t, save
		saved += save
		if t <= 0:
			break
		
#	print unsaved, saved, t
	print "%.9f" % (unsaved - saved)
			