from sys import stdin, stdout

def test(X, R, C):

	if (R * C) % X != 0:
		return "RICHARD"

	R, C = sorted([R, C])

	if X == 3 and R == 1: # too narrow (R can play bent piece)
		return "RICHARD"

	if X == 4 and R <= 2: # too narrow (R can play trapping pieces)
		return "RICHARD"

	return "GABRIEL"


T = int(stdin.readline())
iteration = 0

while (iteration != T):
    X, R, C = map(int, stdin.readline().strip().split())

    iteration += 1
    print "Case #%d: %s"%(iteration, test(X, R, C))
