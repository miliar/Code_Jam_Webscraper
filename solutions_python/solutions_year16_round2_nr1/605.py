import sys
sys.setrecursionlimit(1500); 

def main():
	name, pathin, pathout = sys.argv

	filein = open(pathin)
	fileout = open(pathout,'w')

	total = int(filein.readline())

	results = []
	for case in range(total):
		seq = filein.readline().split()[0]
		results.append(solve(seq))


	for i, result in enumerate(results):
		fileout.write('Case #%s: %s\n'%(i+1, result))

def solve(seq):
	di = {}
	for char in seq:
		di[char] = di.get(char, 0) + 1

	
	resdi = {}
	if di.get('Z',0) > 0:
		n = di['Z']
		for char in 'ZERO':
			di[char] -= n
		resdi[0] = n

	if di.get('W',0) > 0:
		n = di['W']
		for char in 'TWO':
			di[char] -= n
		resdi[2] = n

	if di.get('U',0) > 0:
		n = di['U']
		for char in 'FOUR':
			di[char] -= n
		resdi[4] = n

	if di.get('X',0) > 0:
		n = di['X']
		for char in 'SIX':
			di[char] -= n
		resdi[6] = n

	if di.get('G',0) > 0:
		n = di['G']
		for char in 'EIGHT':
			di[char] -= n
		resdi[8] = n

	if di.get('S',0) > 0:
		n = di['S']
		for char in 'SEVEN':
			di[char] -= n
		resdi[7] = n

	if di.get('F',0) > 0:
		n = di['F']
		for char in 'FIVE':
			di[char] -= n
		resdi[5] = n

	if di.get('T',0) > 0:
		n = di['T']
		for char in 'THREE':
			di[char] -= n
		resdi[3] = n

	if di.get('O',0) > 0:
		n = di['O']
		for char in 'ONE':
			di[char] -= n
		resdi[1] = n

	if di.get('I',0) > 0:
		n = di['I']
		for char in 'NINE':
			di[char] -= n
		resdi[9] = n

	res = ''
	for i in range(10):
		if i in resdi:
			res += resdi[i]*str(i)

	return res

if __name__ == '__main__':
	main()

