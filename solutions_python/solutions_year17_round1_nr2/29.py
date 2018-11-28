from fractions import Fraction
import math

def solve(ingredients,packages):
	packages = [sorted(package) for package in packages]
	
	count = 0
	
	ingredient_minima = [
		(9*x+9) / 10 for x in ingredients
	]
	
	ingredient_maxima = [
		(11*x) / 10 for x in ingredients
	]
	
	while all(len(package) > 0 for package in packages):
		
		min_servings = Fraction(packages[0][0], ingredients[0])*Fraction(10,11)
		max_servings = Fraction(packages[0][0], ingredients[0])*Fraction(10,9)
		
		for i in range(1,len(packages)):
			row = packages[i]
			
			cur_min = Fraction(packages[i][0], ingredients[i])*Fraction(10,11)
			cur_max = Fraction(packages[i][0], ingredients[i])*Fraction(10,9)
			
			min_servings = max(cur_min, min_servings)
			max_servings = min(cur_max, max_servings)
			
		min_servings = int(math.ceil(min_servings))
		max_servings = int(math.floor(max_servings))
		
		if max_servings >= min_servings:
			count += 1
			
			kit = []
			for i in range(len(packages)):
				kit.append(packages[i][0])
				packages[i] = packages[i][1:]
		
		else:
			for i in range(len(packages)):
				cur_min = Fraction(packages[i][0], ingredients[i])*Fraction(10,11)
				cur_max = Fraction(packages[i][0], ingredients[i])*Fraction(10,9)
				if int(math.floor(cur_max)) < min_servings:
					packages[i] = packages[i][1:]
				
	print count


case_count = input()
for case in range(1,case_count+1):
	print 'Case #%d:' % case,
	
	n,p = map(int,raw_input().split(' '))
	ingredients = map(int, raw_input().split(' '))
	packages = [map(int, raw_input().split(' ')) for _ in range(n)]
	
	solve(ingredients,packages)