inp = open("D-large.in", "r")
#inp = open("input.txt", "r")
R=lambda:map(float, inp.readline().strip().split(' '))
f = open("output.txt", "w")

T = int(R()[0])

def strategy_a(arr_a, arr_b):
	arr_a.sort()	
	arr_b.sort()

	num_a = len(arr_a) - 1
	num_b = num_a
	score = 0
	for i in range(len(arr_a)):
		if arr_a[num_a] > arr_b[num_b]:
			score += 1
			num_a -= 1
			num_b -= 1
		else:
			num_b -= 1
	return score

cnt = 0
while cnt < T:
	cnt += 1
	num = int(R()[0])
	arr_a = sorted(R())
	arr_b = sorted(R())

	f.write("Case #%d: %d %d\n" % (cnt, strategy_a(arr_a, arr_b), num - strategy_a(arr_b, arr_a)))
	#print strategy_a(arr_a, arr_b)
	#print num - strategy_a(arr_b, arr_a)
