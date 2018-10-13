import sys

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

cases = input.readline()
cases = int(cases)

def gst(l):
	st = 0
	steps = []
	for x in range(len(l)):
		steps.append(0)

	for x in l:
		if steps[int(x)-1] == 0:
			st = 0
			t = int(x)
			found = []
			if int(x)-1 != l.index(x):
				while t not in found:
					found.append(t)
					t = l[int(x)-1]
					st += 1
			for y in found:
				steps[int(y)-1] = st
	return steps

def fact(x):
	ans = 1
	for y in range(1, x+1):
		ans *= y
	return ans

denominators = [4]
numerators = []
counter = 4

for x in range(100):
	if counter%2: denominators.append(denominators[-1]*counter + 1)
	else: denominators.append(denominators[-1]*counter - 1)
	counter += 1
	
for x in range(3, 105):
	numerators.append(fact(x))
	
ratios = []
for x in range(len(denominators)):
	ratios.append(1.*numerators[x]/denominators[x])
ratios.insert(0, 2.0)
	
for x in range(cases):
	
	cur = int(input.readline())
	list = input.readline().split()
	
	steps = gst(list)
	nums = []
	
	
	for y in range(200):
		nums.append(steps.count(y))
	
	flips = 0
	for z in range(2, len(ratios)):
		flips += nums[z]*ratios[z-2]/z
	
	
	print nums[:5]
	
#	print denominators[:5]
#	print numerators[:5]
#	print steps
	print flips

		
	print ratios[:5]

	output.write("Case #%i: %.6f\n" % (x+1, flips))

input.close()
output.close()


