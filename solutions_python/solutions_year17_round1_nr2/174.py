import sys

def solve(recipe, ingredients):
	for ingr in ingredients:
		ingr.sort()
	kits = 0
	servings = 1
	while True:
		for x in range(len(recipe)):
			while .9*servings*recipe[x] > ingredients[x][0]:
				del ingredients[x][0]
				if len(ingredients[x]) == 0:
					return kits
			if ingredients[x][0] > servings*recipe[x]*1.1:
				servings += 1
				break
			else:
				pass # good
		else:
			kits += 1
			for x in range(len(recipe)):
				del ingredients[x][0]
				if len(ingredients[x]) == 0:
					return kits

T = int(input())
for case in range(T):
	N,P = map(int, input().split())
	recipe = list(map(int, input().split()))
	ingredients = [list(map(int, input().split())) for _ in range(N)]
	op = "Case #{}: {}".format(case+1, solve(recipe, ingredients))
	print(op)
	sys.stderr.write(op + "\n")
