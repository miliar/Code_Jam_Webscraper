import sys

def cookietime(t, farms, X, F):
    return float(X) / (farms*F + 2) + t

def cook(C, F, X):
	now = 0
	number_of_farms = 0
	current_best = cookietime(now, number_of_farms, X, F)
	now += float(C)/(number_of_farms * F + 2)
	number_of_farms += 1
	current = cookietime(now, number_of_farms, X, F)
	while (current < current_best):
		current_best = current
		now += float(C)/(number_of_farms * F + 2)
		number_of_farms += 1
		current = cookietime(now, number_of_farms, X, F)
	print(current_best)

i = 0
for every_line in sys.stdin:
	if (i == 0):
		i += 1
		continue
	line = every_line.strip("\n").split(" ")
	print("Case #" + str(i) + ": ", end = "")
	cook(float(line[0]), float(line[1]), float(line[2]))
	i += 1


