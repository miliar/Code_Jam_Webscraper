def ggd(a, b):
    a, b = max(a, b), min(a, b)
    while a%b<>0:
	a, b = b, a%b
    return b

C = int(raw_input())
for c in range(1, C+1):
    S = map(int, raw_input().split())
    N, T = S[0], S[1:]
    D = []
    T.sort()
    for i in range(N-1):
	if (T[i+1]-T[i])<>0:
	    D.append(T[i+1] - T[i])
    while len(D)>1:
	t = ggd(D[0], D[1])
	del(D[0])
	D[0] = t
    t = D[0]
    Y = map(lambda x: (t - x%t)%t, T)
    y = max(Y)
    print "Case #%d: %d" % (c, y)
