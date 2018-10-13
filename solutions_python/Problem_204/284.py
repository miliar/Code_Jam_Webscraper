import math

t = int(input())

def f(pk, r):
	return int(math.ceil(pk/(1.1*r))),int(math.trunc(pk/(0.9*r)))


def g(x):
	return x[0]*99999999999999+x[1]-x[0]

for k in range(t):
	n, p = [int(i) for i in input().split()]
	r = [int(i) for i in input().split()]
	ings = []
	ings_int = []
	curr_id_ing = []
	for j in range(n):
		ings.append([int(i) for i in input().split()])
		ings_int.append([])
		curr_id_ing.append(0)


	for i in range(n):
		for package in ings[i]:
			n0, n1 = f(package, r[i])
			if n1 - n0 >= 0:
				ings_int[i].append((n0,n1))
			else:
				pass

	for i in range(len(ings_int)):
		ings_int[i] = sorted(ings_int[i], key=g)

	res = 0



	while 1:

		quit = False
		for i in range(len(curr_id_ing)):
			if (curr_id_ing[i] >= len(ings_int[i])):
				quit = True
				break
		if quit:
			break

		take = False
		ints = []
		for i in range(n):
			ints.append(ings_int[i][curr_id_ing[i]])
		mn = min(ints, key=g)
		w = ints.index(mn)

		for i in range(mn[0],mn[1]+1):
			found = True
			for j in range(len(ints)):
				if not ints[j][0] <= i <= ints[j][1]:
					found = False
					break
			if found == True:
				take = True
				break

		if take:
			res += 1
			for i in range(len(ints)):
				curr_id_ing[i] += 1
		else:
			curr_id_ing[w] += 1


	print("Case #" + str(k+1) + ": " + str(res))





