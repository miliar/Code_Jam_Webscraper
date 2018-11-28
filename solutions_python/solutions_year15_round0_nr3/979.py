#-*- coding: utf-8 -*-

#1 = 1
#2 = i
#3 = j
#4 = k
_premap = {
	1: {1: 1, 2:  2, 3:  3, 4:  4},
	2: {1: 2, 2: -1, 3:  4, 4: -3},
	3: {1: 3, 2: -4, 3: -1, 4:  2},
	4: {1: 4, 2:  3, 3: -2, 4: -1},

	# negativos
	-1: {1: 1, 2:  2, 3:  3, 4:  4},
	-2: {1: 2, 2: -1, 3: -4, 4:  3},
	-3: {1: 3, 2:  4, 3: -1, 4: -2},
	-4: {1: 4, 2: -3, 3:  2, 4: -1}

}

pattern = [2, 3, 4]

def solve(L):
	n = len(L)
	
	if n < 4:
		if L == pattern:
			return "YES"
		return "NO"

	j = n
	i = 0
	a = 0

	while j:

		a = L.pop(0)
		j -= 1

		if j == 0:
			break

		b = L.pop(0)
		j -= 1

		c = _premap[a][b]

		if c == pattern[i] and i < 2:
			i += 1

		else:
			L.insert(0, c)
			j += 1

	if i == 2 and abs(a) == 4:
		return "YES"

	return "NO"


def main():
	T = int(raw_input())
	case = 0

	while case < T:
		case += 1

		line1 = raw_input().split(" ")
		line2 = [int(x) for x in raw_input().replace("i", "2").replace("j", "3").replace("k", "4")]

		n = int(line1[1])

		result = solve(line2 * n)

		print "Case #%d: %s" % (case, result)

main()