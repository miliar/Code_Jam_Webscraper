import sys

lines = sys.stdin.readlines()

def dec(a,i):
	if (i<0):
		return
	if a[i]==0:
		a[i] = 9
		dec(a,i-1)
	else:
		a[i] = a[i]-1

T = int(lines[0])
line = 1

for C in range(1,T+1):
	s = [int(c) for c in lines[line].strip()]
	line+=1
#	print(s)

	if len(s)>1:
		r = len(s)-1
		while True:
			ix = 0
			while ix<len(s)-1 and s[ix]<=s[ix+1]:
				ix+=1
#			print("End at", ix, s)
			if (ix<len(s)-1):
				dec(s,ix)
#				print("Decrements", ix, s)
				r = ix+1
				while r<len(s):
					s[r]=9
					r+=1
#				print s
			else:
#				print("Sorted r=",r)
				break
	while len(s)>0 and s[0]==0:
		s=s[1:]
#	print(s)

	sol = "".join([str(c) for c in s])
	print "Case #%d: %s" % (C, sol)
