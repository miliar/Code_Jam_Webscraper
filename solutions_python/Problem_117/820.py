
def solution(a):

	while True:
		if sum(len(x) for x in a) == 0:
			return True

		# Find min
		_min = min([min(x) for x in a])
		_pos_min = None
		for i in xrange(len(a)):
			if _min in a[i]:
				_pos_min = a[i].index(_min),i #coluna/linha
				break

		# Check row
		rb = sum(1 for c in a[_pos_min[1]] if c == _min) == len(a[_pos_min[1]])

		# Check column
		s = 0
		for linha in a:
			if linha[_pos_min[0]] == _min:
				s += 1
		cb = s == len(a)

		# No case
		if [cb,rb] == [False,False]:
			return False
			break
		# Clean the the column that is good
		elif cb:
			for linha in a:
				del linha[_pos_min[0]]
			continue
		# Clean the the row that is good
		elif rb:
			del a[_pos_min[1]]
			continue

		
"""
def solve(a):
	borders = list()
	not_borders = list()
	for b in xrange(min(len(a),len(a[0]))/2):
		borders_aux = list()
		not_borders_aux = list()
		if b >= len(a)-b or b >= len(a[0])-b: 
			break
		for i in xrange(b,len(a)-b):
			for j in xrange(b,len(a[i])-b):
				if i == b or j == b or i == len(a)-b-1 or j == len(a[i])-b-1:
					borders_aux.append(a[i][j])
				else:
					not_borders_aux.append(a[i][j])
		if b > 0:
			if max(borders_aux) < min(borders):
				return False
		borders = borders_aux
		not_borders = not_borders_aux

	return True
"""

T = int(raw_input())
for i in xrange(T):
	N,M = map(int, raw_input().split())
	a = [map(int, raw_input().split()[:M]) for n in xrange(N)]
	print "Case #{0}: {1}".format(i+1, "YES" if solution(a) else "NO")
