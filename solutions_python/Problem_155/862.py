f = open("Ain.txt","r")
g = open("Aout.txt","w")
t = int(f.readline())
for i in xrange(1,t+1):
	st = f.readline().split()[1]
	ans = 0
	cur = 0
	for j in xrange(len(st)):
		if cur < j:
			ans += 1
			cur += 1
		cur += int(st[j])
	g.write("Case #%d: %d\n" % (i,ans))