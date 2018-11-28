from operator import mul
from functools import reduce

t = int(input())
for test in range(t):
	n,k = [int(a) for a in input().split()]
	power = float(input())
	cores = [float(a) for a in input().split()]
	cores.sort()
	while power > 0.00000000001:
		nb_min = cores.count(cores[0])
		if nb_min < len(cores):
			next_step = cores[nb_min]
		else:
			next_step = 1.0
		give_per_c = min((next_step-cores[0])*nb_min,power)/nb_min
		for c in range(nb_min):
			cores[c] += give_per_c
		power -= give_per_c*nb_min
	print("Case #{}: {}".format(test+1, reduce(mul, cores, 1.0)))