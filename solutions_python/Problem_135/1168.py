import sys
import os

in_file = str(sys.argv[1]) 
out_file = os.path.splitext(in_file)[0] + '.out'

fin = open(in_file, 'r')
nr_of_cases = int(fin.readline())

fout = open(out_file, 'w')

cases_done = 0
while cases_done < nr_of_cases:
	cases_done += 1
	rows = []
	for i in xrange(2):
		picked_row = int(fin.readline())
		for j in xrange(1, 5):
			if j == picked_row:
				rows.append(set(fin.readline().split()))
			else:
				fin.readline()
	
	inters = rows[0].intersection(rows[1])
	nr_inters = len(inters)
	if nr_inters == 1:
		answer = inters.pop()
	elif nr_inters > 1:
		answer = 'Bad magician!'
	else:
		answer = 'Volunteer cheated!'

	fout.write('Case #{0}: '.format(cases_done))
	fout.write('{0}'.format(answer))
	fout.write('\n')
	
fin.close()
fout.close()
