import sys

total = int(sys.stdin.readline())

def process(d,n):
	time = []
	for i in range(n):
		params = sys.stdin.readline().split()
		k = int(params[0])
		s = int(params[1])
		time.append((d-k)/s)
	tmin = max(time)
	return (d/tmin)


for i in range (1,total+1):
	params = sys.stdin.readline().split()
	d = int(params[0])
	n = int(params[1])
	ans = process(d,n)
	print("Case #%s: %.6f"%(i,ans))

