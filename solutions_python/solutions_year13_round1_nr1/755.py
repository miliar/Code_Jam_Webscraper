import fileinput

def colorNext(r):
	return 2 * r + 1
	
def solve():
	inf = open('ang')
	content = inf.readlines()
	inf.close()
	outf = open('out', 'w')
	T = int(content[0])
	for i in range(T):
		r = int(content[i+1].split()[0])
		t = int(content[i+1].split()[1])
		color = 2 * r + 1
		
		
		cnt = 0
		while t > 0:
			t -= colorNext(r)
			if t < 0:
				break;
			cnt += 1
			r += 2
			
		outf.write('Case #%d: %d\n'%(i+1, cnt))

solve()