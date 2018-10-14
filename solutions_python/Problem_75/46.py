import sys

data = sys.stdin.readlines()
tests = int(data[0])

def solve(s):
	s = s.split()
	prod = {}
	anti = {}

	k = int(s[0])
	s = s[1:]
	for i in range(k):
		p = s[0]
		s = s[1:]
		prod[(p[0],p[1])] = p[2]
		prod[(p[1],p[0])] = p[2]
	
	k = int(s[0])
	s = s[1:]
	for i in range(k):
		a = s[0]
		s = s[1:]
		if a[0] not in anti:
			anti[a[0]] = ''
		anti[a[0]] = anti[a[0]] + a[1]
		if a[1] not in anti:
			anti[a[1]] = ''
		anti[a[1]] = anti[a[1]] + a[0]

	output = []
	k = int(s[0])
	s = s[1]
	l = []
	for i in range(k):
		l = l + [s[i]]
		changed = False
		while (len(l) >= 2) and (l[-1],l[-2]) in prod:
			l = l[:-2] + [prod[(l[-1],l[-2])]]
			changed = True
		if (not changed) and l[-1] in anti:
#		if l[-1] in anti:
			a = anti[l[-1]]
			for c in a:
				if c in l[:-1]:
					l = []
					break 
			
	return l	

for i in range(1,tests+1):
	result = solve(data[i])
	sys.stdout.write("Case #%d: ["%(i))
	if result != []:
		sys.stdout.write(result[0])
	for i in range(1,len(result)):
		sys.stdout.write(", %c"%(result[i]))
	sys.stdout.write("]\n")
