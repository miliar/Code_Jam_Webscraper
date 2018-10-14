nbTests = int(input())
INFINI = 100000000000

def retourner(pancakes, k, position):
	if k+position <= len(pancakes):
		for i in range(position, position+k):
			if pancakes[i] == "-":
				pancakes[i] = "+"
			else:
				pancakes[i] = "-"

	return pancakes



def calculer(pancakes, k, position):
	if position == len(pancakes):
		if not("-") in pancakes:

			return 0
		else:
			return INFINI

	minimum = calculer(pancakes, k, position+1)
	pancakes = retourner(pancakes, k, position)

	minimum = min(minimum, calculer(pancakes, k, position+1)+1)

	pancakes = retourner(pancakes, k, position)
	
	return minimum


def resoudre(pancakes, k):
	return calculer(pancakes, k, 0)



for i in range(1, nbTests+1):
	pancakes, k = input().split()
	k = int(k)
	pancakes = list(pancakes)

	minimum = resoudre(pancakes, k)
	if minimum == INFINI:
		minimum = "IMPOSSIBLE"

	print("Case #{}: {}".format(i, minimum))