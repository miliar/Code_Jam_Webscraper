
def get_rows():
	rows_1 = list()
	for row_num in range(num_rows):
		rows_1.append([int(x) for x in f.readline().split(" ")])

	return rows_1

out_file = open('a_out.txt', 'w')

def out(case_idx, text):
	print("Case #%d: %s" % (case_idx + 1, text), file=out_file)

with open('A-small-attempt1.in') as f:
	num_rows = 4
	num_cases = int(f.readline())
	for i in range(num_cases):
		answer_1 = int(f.readline())
		rows_1 = get_rows()
		answer_2 = int(f.readline())
		rows_2 = get_rows()
		
		cards = set(rows_1[answer_1 - 1]).intersection(set(rows_2[answer_2 - 1]))
		
		if len(cards) == 1:
			out(i, cards.pop())
		elif len(cards) > 1:
			out(i, "Bad magician!")
		else:
			out(i, "Volunteer cheated!")

