

def check_h(h):
	global H, N, M
	for l in H:
		if min(l) > h: continue
		for i in xrange(M):
			if l[i] > h and l[i] != 100: break
		else: 
			l = [100] * M
			continue
		for i in xrange(M):
			if l[i] == h:
				for j in xrange(N):
					if H[j][i] > h and H[j][i] != 100: return False
					H[j][i] = 100
	return True


f = open('in','r')
T = int(f.readline())
for t in xrange(T):
	N, M = (int(x) for x in f.readline().split())
	H = []
	for n in xrange(N):
		l = list(int(x) for x in f.readline().split())
		H.append(l)
	for h in xrange(1,100):
		if not check_h(h): 
			print 'Case #' + str(t+1) + ': NO'
			break
	else: print 'Case #' + str(t+1) + ': YES'
		
				
	
		
