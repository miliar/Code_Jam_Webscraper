from stalls import stalls
f = open('in.in', 'r')
T = int(f.readline())
ans = ""
for i in range(T):
	line = f.readline()
	linelist = line.split(" ")
	N = int(linelist[0])
	K = int(linelist[1])
	ansT = stalls(N, K)
	ans += ("Case #%d: %d %d\n" % (i+1, ansT[0], ansT[1]))
print(ans)
fo = open('out.out', 'w')
fo.write(ans)
