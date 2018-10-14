from sys import argv, setrecursionlimit

def get_time(c, f, x, rate = 2):
	time0 = x/rate
	next_frame = c/rate
	next_rate = rate+f
	time1 = next_frame + x/next_rate
	if time0 < time1:
		return time0
	else:
		return next_frame + get_time(c, f, x, next_rate)

with open(argv[1]) as f:
	f.readline()
	i = 1
	for ligne in f:
		c, f, x = tuple(ligne.strip().split(' '))
		c, f, x = float(c), float(f), float(x)
		best_time = 0
		rate = 2
		while True:
			#print(rate)
			time0 = x/rate
			next_frame = c/rate
			next_rate = rate+f
			time1 = next_frame + x/next_rate
			if time0 < time1:
				best_time += time0
				break
			else:
				best_time += next_frame
				rate += f
		print("Case #%d: %.7f" % (i, best_time))
		i += 1