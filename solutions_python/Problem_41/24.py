import os, sys

fi = open('B-large.in', 'r')
fo = open('b.out', 'w')

def test_case(ncase):
	num = list(fi.readline().rstrip())
	lc = ' '
	sofar = []
	for i, c in list(enumerate(num))[::-1]:
		#print i, c, lc
		if c >= lc:
			lc = c
			sofar.append(c)
		else:
			sofar.sort()
			for j, k in enumerate(sofar):
				if k > c:
					sofar[j] = c
					num[i] = k
					num[i+1:] = sorted(sofar)
					break
			break
	else:
		num.sort()
		nc = num.count('0')
		num = filter(lambda x: x != '0', num)
		num = [num[0]] + ['0'] * (nc + 1) + num[1:]
	print >>fo, 'Case #%d: %s' % (ncase, ''.join(num))

nc = int(fi.readline())
for i in range(1, nc+1):
	test_case(i)

fo.close()