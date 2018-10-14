from sets import Set

class Strings:
	bad_magician = "Bad magician!"
	volunteer_cheat = "Volunteer cheated!"

def get_card_board():
	board = []
	for i in xrange(4):
		board.append([int(i) for i in raw_input().split()])
	return board


def solve_problem(test_no):
	volun_answer = int(raw_input())
	card_board = get_card_board()

	first_row = Set(card_board[volun_answer - 1])

	volun_answer = int(raw_input())
	card_board = get_card_board()

	second_row = Set(card_board[volun_answer - 1])

	first_row.intersection_update(second_row)
	substitutions = len(first_row)

	if substitutions == 0:
		print "Case #%d: %s" % (test_no, Strings.volunteer_cheat)
	elif substitutions == 1:
		print "Case #%d: %d" % (test_no, first_row.pop())
	else:
		print "Case #%d: %s" % (test_no, Strings.bad_magician)


test_cases = int(raw_input())
for i in xrange(test_cases):
	solve_problem(i+1)