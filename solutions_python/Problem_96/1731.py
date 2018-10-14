fin = open('B-large.in', 'r')
fout = open('b.out', 'w')

cases = int(fin.readline().strip())

for i in range(cases):
	parts = fin.readline().strip().split(' ')

	dancers = int(parts[0])
	surp = int(parts[1])	

	min_score = int(parts[2])
	min_score_1 = min_score - 1 if min_score - 1 >= 0 else 0
	min_score_2 = min_score - 2 if min_score - 2 >= 0 else 0

	success = 0
	
	for d in range(dancers):
		score = int(parts[3 + d])
		
		if min_score + (min_score_1) * 2 <= score:
			success += 1
		elif surp > 0 and min_score + (min_score_2) * 2 <= score:
			success += 1
			surp -= 1
	
	fout.write("Case #%d: %d\n" % ((i + 1), success))

fin.close()
fout.close()
