C = int(raw_input())
for c in range(1, C+1):
    N = int(raw_input())
    A, B = [], []
    for n in range(N):
	t = map(int, raw_input().split())
	A.append(t[0])
	B.append(t[1])	
    s = 0
    for i in range(N):
	for j in range(N):
	    if A[i]>A[j] and B[i]<B[j]:
		s = s + 1           

    print "Case #%d: %d" % (c, s)
