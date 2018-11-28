
fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

T = int(fin.readline())
for t in range(0, T):
	N, K = map(int, fin.readline().split())
	state = 'ON' if K % (2**N) == (2**N)-1 else 'OFF'
	fout.write("Case #%d: %s\n" % (t+1, state))


