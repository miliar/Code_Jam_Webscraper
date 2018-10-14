#! /usr/bin/python

def tidy(n):
	changed=True
	while changed:
		changed=False
		for i in range(len(n)-1):
			if n[i] > n[i+1]:
				n[i]-=1
				for j in range(i+1,len(n)):
					n[j]=9
				changed=True			
	return int("".join(map(str,n)));

t = int(raw_input().strip())
for i in range(t):
	n = map(int,raw_input().strip())
	print "Case #%i: %i" % (i+1,tidy(n))