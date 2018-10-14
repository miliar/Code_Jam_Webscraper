from __future__ import print_function
import sys

def arrange(myin):
	# print myin
	n, r, o, y, g, b, v = [int(i) for i in myin]
	common = 0
	res = ""

	if b<o+1 or r<g+1 or y<v+1:
		return 'IMPOSSIBLE'
		

	if r >= y and r >= b:
		if r > y+b:
			return 'IMPOSSIBLE'
		common = y+b-r

		for i in xrange(common):
			res += 'RYB'
		while b-common>0:
			res += 'RB'
			b-=1
		while y-common>0:
			res += 'RY'
			y-=1

	elif y>=r and y>=b:
		if y > r+b:
			return 'IMPOSSIBLE'
		common = b+r-y
		for i in xrange(common):
			res += 'YRB'
		while b-common>0:
			res += 'YB'
			b-=1
		while r-common>0:
			res += 'YR'
			r-=1


	elif b>=r and b>=y:
		if b > r+y:
			return 'IMPOSSIBLE'
		common = r+y-b
		for i in xrange(common):
			res += 'BRY'
		while r-common>0:
			res += 'BR'
			r-=1
		while y-common>0:
			res += 'BY'
			y-=1

	return res




# here start the main program
if __name__=='__main__':
	cases = -1
	cnt = 1
	file = sys.argv[1]

	rem = 0

	# open the file and call the largest tidy number and valid tidy number
	with open(file) as fin:
		for line in fin:
			if cases == -1:
				cases = line
			else:
				myin = line.split(' ')
				res = arrange(myin)
				print('Case #%d: %s' % (cnt, res))
				cnt += 1
