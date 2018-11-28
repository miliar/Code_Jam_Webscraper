import sys

def dwar(lst_1, lst_2):
	score = 0
	while len(lst_1):
		if lst_1[0] > lst_2[0]:
			score += 1
			lst_1.pop(0)
			lst_2.pop(0)
		else:
			lst_1.pop(0)
			lst_2.pop()
	return score

def war(lst_1, lst_2):
	score = 0
	while len(lst_1):
		if lst_1[0] > lst_2[-1]:
			score += len(lst_1)
			break
		else:
			for i in range(len(lst_1)):
				if lst_2[i] > lst_1[0]:
					lst_2.pop(i)
					lst_1.pop(0)
					break
	return score


input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

cases = int(input_file.readline().strip())
for case in range(cases):
	input_file.readline()
	lst_naomi = sorted(list(map(float, input_file.readline().strip().split())))
	lst_ken = sorted(list(map(float, input_file.readline().strip().split())))
	lst_naomi_c = [i for i in lst_naomi]
	lst_ken_c = [i for i in lst_ken]
	output_file.write('Case #%d: %d %d\n' % (case + 1, dwar(lst_naomi, lst_ken), war(lst_naomi_c, lst_ken_c)))

input_file.close()
output_file.close()

