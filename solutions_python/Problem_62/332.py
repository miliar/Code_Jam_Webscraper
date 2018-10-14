
f = open("A-small-attempt0.in","r")
w = open("outa.txt","w")
Cases = int(f.readline())
for case in range(1, Cases+1):	
	N = int(f.readline())
	M = {}
	ans = 0
	for n in range(0, N):
		M[n] = map(int, f.readline().split())
	
	for n in range(0, N):
		a = M[n]
		n += 1
		for m in range(n, N):
			b = M[n]
			if a[0] > b[0] and a[1] < b[1] or a[0] < b[0] and a[1] > b[1]:
				ans += 1
	
	w.write("Case #%d: %d\n" % (case,ans))
	#print "Case #%d: %d" % (case,ans)
f.close()
w.close()