def pancakes(P):
	if max(P) <= 2:
		return max(P)
	
	eat = [p - 1 for p in P]
	m = max(P)
	i = P.index(m)
	P[i] /= 2
	special = list(P + [m - P[i]])

	if m >= 9:
		P[i] = 2 * m / 3
		special2 = list(P + [m - P[i]])
		return 1 + min(pancakes(eat),  pancakes(special), pancakes(special2))

	return 1 + min(pancakes(eat),  pancakes(special))

def main():
	from sys import stdin
	input = stdin.read().split('\n')
	T = int(input[0])

	for t in range(T):
		D = int(input[2 * t + 1])
		P = map(int, input[2 * t + 2].split())

		print "Case #{0}: {1}".format(t + 1, pancakes(P))

if __name__ == '__main__':
	main()