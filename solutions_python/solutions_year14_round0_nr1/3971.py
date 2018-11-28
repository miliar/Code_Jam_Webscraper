
def readFile(filename):

	final_answers = []
	case_no = 1

	answers_file = open("magician_answers.text", "w")
	with open(filename) as f:
		next(f)
		ind = 0
		answers = []
		rows1 = []
		rows2 = []
		for line in f:

			if ind == 0 or ind == 5:
				answers.append(line.strip())
				ind += 1
				continue
			row = line.split(" ")
			row[3] = row[3].strip()
			if ind <= 4:
				rows1.append(row)
			if ind > 4:
				rows2.append(row)
			if ind == 9:
				answer = magicianJudgement(answers, rows1, rows2)
				answers_file.write("Case #" + str(case_no) + ": " + answer + "\n")
				ind = 0
				# print answers
				# print rows1
				# print rows2
				answers = []
				rows1 = []
				rows2 = []
				case_no += 1
				continue
			ind += 1




def magicianJudgement(answers, rows1, rows2):
	first_answer = int(answers[0]) - 1
	possible_row = rows1[first_answer]
	second_answer = int(answers[1]) - 1

	possible_answers = 0
	answer_val = ""
	for card1 in possible_row:
		for card2 in rows2[second_answer]:
			# print card1
			# print card2
			if card1 == card2:
				possible_answers += 1
				answer_val = card1
	if (possible_answers == 1):
		return answer_val
	if (possible_answers > 1):
		return "Bad magician!"
	if (possible_answers == 0):
		return "Volunteer cheated!"


	

readFile("A-small-attempt0.in")
