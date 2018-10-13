from pancakes import pancakes
f = open('in.in', 'r')
T = int(f.readline())
ans = ""
for i in range(T):
	line = f.readline()
	linelist = line.split(" ")
	S = linelist[0]
	K = int(linelist[1])
	ansN = pancakes(S, K)
	if ansN == -1:
		ansN = "IMPOSSIBLE"
	ans += ("Case #%d: %s\n" % (i+1, ansN))
print(ans)
fo = open('out.out', 'w')
fo.write(ans)
