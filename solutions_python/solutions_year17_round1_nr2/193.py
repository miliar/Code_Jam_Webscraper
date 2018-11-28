import math

def make_kits(num_ingredients, num_packages, ingredients_proportion, packages):
	for i in xrange(0, num_ingredients):
		packages[i].sort()
	counter = 0
	pointers = [0]*num_ingredients
	for i in xrange(0, num_packages):
		num_servings = serving(packages[0][i], ingredients_proportion[0])
		# print "i: ", i, " num_servings: ", num_servings
		for num_serving in xrange(num_servings[0], num_servings[1]+1):
			flag = 0
			for j in xrange(1, num_ingredients):
				while pointers[j] < num_packages and too_little(packages[j][pointers[j]], ingredients_proportion[j], num_serving):
					pointers[j] = pointers[j]+1
				if pointers[j] == num_packages or too_much(packages[j][pointers[j]], ingredients_proportion[j], num_serving):
					flag = -1
					break
			if flag == 0:
				# print "counter: ", counter
				# print i, " ", pointers[1]
				pointers = [x+1 for x in pointers]
				counter = counter+1
				break		
	return counter


def serving(weight, unit):
	res = []
	res.append(int(math.ceil(weight/1.1/unit)))
	res.append(int(math.floor(weight/0.9/unit)))
	return res

def too_little(weight, unit, num_serving):
	if weight < unit*num_serving*0.9:
		return True
	return False

def too_much(weight, unit, num_serving):
	if weight > unit*num_serving*1.1:
		return True
	return False



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  num_ingredients, num_packages = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  ingredients_proportion = [int(s) for s in raw_input().split(" ")]
  packages = [[] for k in xrange(1, num_ingredients+1)]
  for j in xrange(0, num_ingredients):
  	packages[j] = [int(s) for s in raw_input().split(" ")]
  res = make_kits(num_ingredients, num_packages, ingredients_proportion, packages)
  print "Case #{}: {}".format(i, res)
  # check out .format's specification for more formatting options


