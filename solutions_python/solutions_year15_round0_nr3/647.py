import sys

def product(a, b):
	if a=='1':
		return b
	elif b=='1':
		return a
	elif a==b:
		return '-1'
	elif a=='k' and b=='i':
		return 'j'
	elif a=='i' and b=='k':
		return '-j'
	elif a=='k' and b=='j':
		return '-i'
	elif a=='j' and b=='k':
		return 'i'
	elif a=='j' and b=='i':
		return '-k'
	elif a=='i' and b=='j':
		return 'k'

def mul(a, b):
	if (len(a) == 1):
		if (len(b) == 1):
			return product(a, b)
		elif (len(b) == 2):
			k = product(a, b[1])
			if (len(k) == 2):
				return k[1]
			else:
				return '-'+k
	elif (len(a) == 2):
		if (len(b) == 1):
			k = product(a[1], b)
			if (len(k) == 2):
				return k[1]
			else:
				return '-'+k
		elif (len(b) == 2):
			return product(a[1], b[1])

t = int(input())
k = 1
while t>0:
	t -= 1
	sys.stdout.write('Case #'+str(k)+': ')
	k += 1
	c, r = [int(a) for a in raw_input().split()]
	s = raw_input()
	s *= r
	prev = '1'
	first = []
	flag = 0
	for x in xrange(0, len(s)):
		prev=mul(prev, s[x])
		if prev == 'i':
			kprev = '1'
			for y in xrange(x+1, len(s)):
				kprev=mul(kprev, s[y])
				if kprev == 'j':
					lprev = '1'
					for z in xrange(y+1, len(s)):
						lprev=mul(lprev, s[z])
					if lprev=='k':
						flag = 1
					break
#			if flag == 1:
			break
	if flag == 1:
		print 'YES'
	else:
		print 'NO'
