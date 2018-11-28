import sys

T = int(sys.stdin.readline().strip())

used = [0] * 20
N = 0
res = -1
N2 = 0

def next_permut(k,perm) :
	global used
	global N
	global res
	global N2
	
	if (k == len(str(N))) :
		if (int(perm) > N2) and ((int(perm) < res) or (res == -1)) :
			res = int(perm)
	else:
		for i in range(0,len(str(N))):
			if (used[i] == 0):
				used[i] = 1
				next_permut(k+1,perm + str(N)[i])
				used[i] = 0
	

for t in range(1,T+1):
	
	N = int(sys.stdin.readline().strip())
	N2 = N
	res = -1
	
	for i in range(0,len(str(N))):
		used[i] = 1
		next_permut(1,str(str(N)[i]))
		used[i] = 0
	
	d = [0] * 10
	
	if (res == -1) :
		N *= 10
		for i in range(0,len(str(N))):
			used[i] = 1
			next_permut(1,str(str(N)[i]))
			used[i] = 0
		
	print 'Case #' + str(t) + ':',res