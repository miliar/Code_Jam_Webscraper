
#import sys

def row2chunks(row):
	return row.replace('\n', '')[1:].split('/')


fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')  # sys.stdout

T = int(fin.readline())
for test in range(0, T):
	N, M = map(int, fin.readline().split())
	avai = [row2chunks(fin.readline()) for _ in range(0, N)]
	
	ans = 0
	for _ in range(0, M):
		nav = row2chunks(fin.readline())
		
		bestd = 0
		for av in avai:
			d = 0
			while d < len(nav) and d < len(av) and av[d] == nav[d]:
				d += 1
			bestd = max(bestd, d)
		
		ans += len(nav) - bestd
		avai.append(nav)
	
	fout.write("Case #%d: %d\n" % (test+1, ans))

