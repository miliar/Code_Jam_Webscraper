# f = open('B-large.in' , 'r')
f = open('D-large.in' , 'r')
n = int(f.readline())
f_out = open('D.out', 'w')

for test_idx in range(1, n+1):
	n = int(f.readline())
	first = map(float, f.readline().split(' '))
	second = map(float, f.readline().split(' '))
	first.sort()
	curr_first = list(first)
	second.sort(reverse=True)
	first_score = 0
	for second_idx in range(n):
		if curr_first[-1] > second[second_idx]:
			for first_idx in range(len(curr_first)):
				if curr_first[first_idx] > second[second_idx]:
					del curr_first[first_idx]
					first_score += 1
					break
		else:
			del curr_first[0]
	y = first_score

	second.sort()
	second_score = 0
	second_idx = 0
	for i in range(n):
		while second_idx < n and first[i] > second[second_idx]:
			second_idx += 1
		if second_idx >= n:
			break
		second_score += 1
		second_idx += 1
	z = n - second_score
	
	f_out.write('Case #' + str(test_idx) + ': ' + str(y) + ' ' + str(z) + '\n')

