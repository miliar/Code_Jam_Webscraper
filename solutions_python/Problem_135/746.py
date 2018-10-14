f = open('A-small-attempt1.in' , 'r')
# f = open('input.txt' , 'r')
n = int(f.readline())
f_out = open('output.txt', 'w')

for test_idx in range(1, n+1):
	row_1_idx = int(f.readline())
	row_1 = []
	row_2 = []
	for idx in range(1, 5):
		line = f.readline()
		if idx == row_1_idx:
			row_1 = map(int, line.split(' '))
	row_2_idx = int(f.readline())
	for idx in range(1, 5):
		line = f.readline()
		if idx == row_2_idx:
			row_2 = map(int, line.split(' '))

	answ = list(set(row_1) & set(row_2))
	f_out.write('Case #' + str(test_idx) + ': ')
	if len(answ) == 0:
		f_out.write('Volunteer cheated!\n')
	elif len(answ) > 1:
		f_out.write('Bad magician!\n')
	else:
		f_out.write(str(answ[0]) + '\n')

