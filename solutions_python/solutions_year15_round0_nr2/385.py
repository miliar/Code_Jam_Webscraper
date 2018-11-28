f = open('B-large.in')
fw = open('B-large.out', 'w')

cases = int(f.readline())
for case in range(cases):
	D = int(f.readline())
	pancakes = f.readline().split()
	
	plates = [0] * 2000
	biggest_pan = 0
	for i in range(D):
		pancakes[i] = int(pancakes[i])
		plates[pancakes[i]] += 1
		if pancakes[i] > biggest_pan:
			biggest_pan = pancakes[i]

	best_move = biggest_pan
	for i in range(1, biggest_pan + 1):
		sep_count = 0
		for j in range(i + 1, biggest_pan + 1):
			sep_count += plates[j] * ((j - 1) / i)
		if sep_count + i < best_move:
			best_move = sep_count + i
	
	fw.write('Case #' + str(case + 1) + ': ' + str(best_move) + '\n')


fw.close()
f.close()
