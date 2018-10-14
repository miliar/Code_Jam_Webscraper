#!/usr/bin/env python3

def lire_ligne():
	i = int(input())
	return [{int(n) for n in input().split()} for _ in range(4)][i - 1]

if __name__ == '__main__':
	T = int(input())

	for i in range(T):
		print("Case #{}: ".format(i + 1), end="")

		possibles = lire_ligne().intersection(lire_ligne())
		N = len(possibles)

		if N == 0:
			print("Volunteer cheated!")

		elif N > 1:
			print("Bad magician!")

		else:
			carte, *_ = possibles
			print(carte)
