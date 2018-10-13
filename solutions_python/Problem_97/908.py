import sys

f = sys.stdin

n = int(f.readline())

for i in range(1, n+1):
	print "Case #{}:".format(i),
	inp = f.readline().rstrip().split(' ')
	a = int(inp[0])
	b = int(inp[1])
	cnt = 0
	
	for m in range(a, b):
			m = str(m)
			l = []
			for k in range(1, len(m)):
				n = m[k:] + m[:k]
				if int(n) > int(m) and int(n) <= b:
					flag = True
					for o in l:
						if n == o:
							flag = False
					
					if flag:
						l.append(n)
						cnt = cnt + 1

	print cnt



