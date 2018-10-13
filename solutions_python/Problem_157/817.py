import sys

yes = 'YES'
no = 'NO'

vec = {
	1: 1,		-1: -1,
	'i': [1, 0, 0],	'-i': [-1, 0, 0],
	'j': [0, 1, 0],	'-j': [0, -1, 0],
	'k': [0, 0, 1],	'-k': [0, 0, -1]
	}

obj = ['i', 'j', 'k']

def mul(a, b):
	p = None
	if a is 1:
		return b
	elif b is 1:
		return a
	elif a is -1:
		if type(b) is int:
			return a * b
		b = vec[b]
		p = [-b[0], -b[1], -b[2]]
	elif b is -1:
		if type(a) is int:
			return a * b
		a = vec[a]
		p = [-a[0], -a[1], -a[2]]
	elif a is b:
		p = -1
	
	if p is None:
		a = vec[a]
		b = vec[b]
		if a[0] * b[0] + a[1] * b[1] + a[2] * b[2] is -1:
			p = 1
		else:
			p = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

	for k in list(vec.keys()):
		if p == vec[k]:
			return k

def isPossible(string):
	# print('String pool: {0}'.format(string))

	currentObj = 0
	currentVal = 1
	for i in range(len(string)):
		# print('Target: {0}'.format(obj[currentObj]))
		ijk = string[i]
		nextVal = mul(currentVal, ijk)
		# print('Do mul({0}, {1}) = {2}'.format(currentVal, ijk, nextVal), sep = '')

		if nextVal is obj[currentObj]:
			# print('Match {0}'.format(obj[currentObj]))
			red = string[i + 1:]
			# print('String remain: {0}'.format(red))
			currentObj += 1
			currentVal = 1

			if currentObj == 3:
				# print('Done. Check redundancy')
				if len(red) is 0:
					return yes
				for r in red:
					currentVal = mul(currentVal, r)
				if currentVal is 1:
					return yes
				return no

			continue

		currentVal = nextVal
	return no

def main():
	fin = open(sys.argv[1], 'rU')
	nCases = int(fin.readline())
	# for c in range(2):
	for c in range(nCases):
		(nAlphabet, nRep) = map(int, fin.readline().strip().split(' '))
		string = list(map(str, fin.readline().strip() * nRep))
		print('Case #{0}: {1}'.format(c + 1, isPossible(string)))



if __name__ == "__main__":
	main()