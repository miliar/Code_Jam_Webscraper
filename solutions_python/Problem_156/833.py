data = '''100
1
3
4
1 2 1 2
1
4
6
3 3 5 5 9 9
5
5 3 2 5 3
3
6 6 3
5
9 9 9 9 9
3
9 8 1
5
5 1 2 2 5
4
2 8 7 5
2
2 1
5
8 9 7 8 2
5
1 2 1 3 1
4
3 5 2 4
3
4 2 7
5
1 3 5 1 3
4
9 9 9 9
2
9 9
6
5 5 5 5 9 9
6
7 7 7 7 7 9
4
3 5 2 6
3
3 4 2
5
5 4 3 2 1
5
5 5 6 3 2
5
3 1 4 5 2
3
1 6 5
2
9 6
2
8 4
6
5 6 9 6 9 6
3
1 4 1
3
9 9 9
3
8 8 8
3
6 6 5
3
2 5 1
6
1 1 5 5 9 9
3
6 6 9
2
9 9
2
6 6
6
5 5 5 9 9 9
3
1 1 4
4
4 4 3 5
2
4 9
3
3 5 3
3
1 8 5
2
5 5
3
9 5 1
3
3 2 1
3
6 5 4
1
4
4
6 1 5 5
4
2 9 7 8
3
1 2 8
2
9 7
4
4 4 3 3
5
5 3 4 2 5
2
7 7
4
9 6 8 4
6
9 9 9 9 9 9
4
1 2 8 5
1
6
4
8 5 5 6
1
1
3
8 5 2
3
7 5 3
2
8 8
3
4 1 5
3
4 5 7
3
6 5 4
4
8 8 8 8
5
2 4 2 2 1
1
5
5
2 1 1 2 3
6
6 5 4 3 2 1
2
9 8
5
3 2 2 3 5
4
5 7 2 8
5
2 3 6 8 3
3
2 4 5
6
6 6 6 6 9 9
3
3 3 9
4
7 3 2 2
3
4 6 2
6
3 6 6 6 9 9
4
3 7 6 1
2
4 8
4
3 1 3 7
6
2 9 9 9 3 3
4
1 2 5 9
5
1 2 5 1 3
1
8
5
8 8 8 8 8
4
5 8 3 6
3
6 7 7
4
2 1 3 5
1
7
4
9 5 2 8
4
4 3 1 8
4
2 7 5 3
4
4 3 2 1
1
9
'''
outstore = []
def getbase(check):
	n = 1
	s = 0
	while check > 0:
		check -= n
		n+=1
	return n-1 if check ==0 else n-2
def findsec(cakes):
	big = max(cakes)
	for x in cakes:
		if x < big:
			return x
	return 0
data = [x for x in data.split('\n') if x]

case_count,data = data[0],data[1:]
for case in range(int(case_count)):
	tables,pancakes,data = data[0],data[1],data[2:]
	# pancakes = sorted(map(int,pancakes.split()),key=lambda x:-1*x)
	pancakes = map(int, pancakes.split())
	# print pancakes
	allset = range(1,max(pancakes)+1)
	minstep = 1000
	for ceiling in allset:
		step = 0
		testtable = pancakes[:]
		biggest = max(testtable)
		while biggest > ceiling:
			testtable.remove(biggest)
			testtable += [ceiling,biggest-ceiling]
			biggest = max(testtable)
			step += 1
		step += ceiling
		if step < minstep:
			minstep = step
	result = 'Case #%d: %d' %(case+1, minstep)
	print result
	outstore.append(result)

with open('output.out','w') as f:
	for line in outstore:
		f.write(line+'\n')




