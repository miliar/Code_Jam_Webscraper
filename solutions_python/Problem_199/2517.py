import sys

n=input()

for case in xrange(1, n+1):
	line = sys.stdin.readline().split()
	s = list(line[0])
	k = int(line[1])
	l=len(s)
	flips=0
	possible=True
	for i in xrange(0, l):
		if s[i]=="-":
			if (k > l-i):
				possible=False
			else:
				flips += 1
				for m in xrange(i, i+k):
					
					if s[m] == "+":
						s[m]="-"
					else:
						s[m]="+"
	if possible:
		solution=str(flips)
	else:
		solution="IMPOSSIBLE"
	print "Case #%s:" % case, solution
	


