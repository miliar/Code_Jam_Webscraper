import sys

def check(n):
	s = str(n)

	l = len(s)
	sr = ""
	for i in range(l):
		sr = sr + s[l-i-1];

	if(s == sr):
		return 1

	return 0

i = 0
c = 0
ok = []
while True:
	#if(i > 32):
	if(i > 10000000):
		break;

	if(check(i)):
		d = i**2
		if(check(d)):
			#if(d <= 1000):
			if(d <= 100000000000000):
				ok.append(d)

	i = i+1

T = int(sys.stdin.readline())

for tc in range(T):
	r = [int(n) for n in sys.stdin.readline().split()]

	res = 0
	for i in range(len(ok)):
		if(ok[i] >= r[0]):
			if(ok[i] <= r[1]):
				res = res+1

	print "Case #%d: %d" % (tc+1, res)
