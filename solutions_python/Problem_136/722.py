f = open('B-large.in' , 'r')
# f = open('B-test.in' , 'r')
n = int(f.readline())
f_out = open('B.out', 'w')

for test_idx in range(1, n+1):
	C, F, X = map(float, f.readline().split(' '))
	rate = 2
	farms_time = 0
	best_time = X / 2
	while farms_time < best_time:
		farms_time += C / rate
		rate += F
		best_time = min(farms_time + X / rate, best_time)

	f_out.write('Case #' + str(test_idx) + ': ' + str(best_time) + '\n')

