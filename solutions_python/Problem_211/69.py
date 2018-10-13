
f = open('ctiny.in')
fout = open('ctiny.out', 'w')
f = open('csmall.in')
fout = open('csmall.out', 'w')

numCases = int(f.readline().strip())


for numCase in range(numCases):
	ss = f.readline().strip().split(' ')
	N = int(ss[0])
	K = int(ss[1])

	U = float(f.readline().strip())
	cores = []
	ss = f.readline().strip().split(' ')
	for i in range(N):
		cores.append(float(ss[i]))

	cores.sort()
	cores.reverse()

	index = 0
	avg = None
	while True:
		avg = (U + sum(cores[index:])) * 1.0 / (N - index)
		if cores[index] <= avg:
			break
		index += 1

	if avg is None:
		raise ValueError('ooo')

	print avg, index

	ret = 1.0
	for i in range(0, index):
		ret *= cores[i]

	ret *= (avg ** (N-index))


	fout.write('Case #{}: '.format(numCase + 1))
	fout.write('{}\n'.format(ret))


fout.close()

"""
4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
2 1
0.0000
0.9000 0.8000
2 1
0.1000
0.4000 0.5000

Case #1: 1.000000
Case #2: 0.250000
Case #3: 0.980000
Case #4: 0.760000



"""

