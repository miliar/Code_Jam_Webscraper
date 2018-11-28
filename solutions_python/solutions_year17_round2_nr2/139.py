import sys


te = input()

for qe in range(1, te+1):

	n,r,o,y,g,b,v = map(int, raw_input().split())

	# small
	# a = [['R', r], ['B', b], ['Y', y]]
	# a.sort(key=lambda x: x[1], reverse=True)

	# if a[1][1]+a[2][1]>=a[0][1]:
	# 	ans = ''
	# 	for _ in range(a[0][1]-a[2][1]):
	# 		ans += a[1][0]+a[0][0]
	# 	for _ in range(a[1][1]+a[2][1]-a[0][1]):
	# 		ans += a[1][0]+a[2][0]+a[0][0]
	# 	for _ in range(a[0][1]-a[1][1]):
	# 		ans += a[2][0]+a[0][0]

	# else:
	# 	ans = 'IMPOSSIBLE'

	if (b > o or o == 0) and (r > g or g == 0) and (y > v or v == 0):

		b -= o
		r -= g
		y -= v


		a = [['R', r], ['B', b], ['Y', y]]
		a.sort(key=lambda x: x[1], reverse=True)

		if a[1][1]+a[2][1]>=a[0][1]:
			ans = ''
			for _ in range(a[0][1]-a[2][1]):
				ans += a[1][0]+a[0][0]
			for _ in range(a[1][1]+a[2][1]-a[0][1]):
				ans += a[1][0]+a[2][0]+a[0][0]
			for _ in range(a[0][1]-a[1][1]):
				ans += a[2][0]+a[0][0]

			# print n,r,o,y,g,b,v
			ans = ans.replace('B', 'B'+'OB'*o, 1)
			ans = ans.replace('R', 'R'+'GR'*g, 1)
			ans = ans.replace('Y', 'Y'+'VY'*v, 1)

		else:
			ans = 'IMPOSSIBLE'
	
	elif o > 0 and b == o and n == 2*o:
		ans = 'BO'*o

	elif g > 0 and r == g and n == 2*g:
		ans = 'RG'*g

	elif v > 0 and y == v and n == 2*v:
		ans = 'YV'*v

	else:
		ans = 'IMPOSSIBLE'

	print >> sys.stderr, str(qe)+'/'+str(te)+' started ...'

	print 'Case #{}: {}'.format(qe, ans)