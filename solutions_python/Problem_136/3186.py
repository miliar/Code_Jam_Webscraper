import math

def compute_1(c, f, x):
	nf = math.floor((x/2)/(c/f))
	rate = 2
	time = 0
	for m in range(nf):
		time += (c/rate)
		rate += f
	return time

def compute_2(c, f, x):
	rate = 2
	time = x/rate
	while True:
		if time - x/rate + c/rate + x/(rate+f) < time:
			time += c/rate + x/(rate+f) - x/rate
			rate += f
		else:
			break
	return time

fin = open("B-large.in", "r")
fout = open("out", "w")
T = int(fin.readline())
for i in range(T):
	[c, f, x] = [float(v) for v in fin.readline().split()]
	time = compute_2(c, f, x)
	fout.write("Case #" + str(i+1) + ": " + str(time) + '\n')
fout.close()