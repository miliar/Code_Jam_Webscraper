

def besttime(c,f,x):
	rate = 2.0
	cont = True
	acc = 0.0
	best_t = x/rate

	while cont:
		if best_t > acc + c/rate + (x/(rate+f)):
			best_t = acc + c/rate + (x/(rate+f))
			acc += c/rate
			rate += f
		else:
			cont = False
	return best_t


test_cases = int(raw_input())
output = []
for i in range(test_cases):
	line = raw_input()
	vals = [ float(x) for x in line.split()]
	best_time = besttime(vals[0],vals[1],vals[2])
	output.append("Case #%d: %f"%(i+1,round(best_time,7)))

for x in output:
	print x
