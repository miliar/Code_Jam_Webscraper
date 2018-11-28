__author__ = 'siddmanu'
import sys


def main():
	line = sys.stdin.readline()
	input_count = int(line)
	case_count = 1
	while input_count > 0:
		line = sys.stdin.readline()
		first_answer = int(line)
		first_cards = set()
		for i in range(4):
			line = sys.stdin.readline().strip()
			if i == first_answer - 1:
				first_cards = set([int(l) for l in line.split(' ')])

		second_answer = int(sys.stdin.readline())
		for i in range(4):
			line = sys.stdin.readline().strip()
			if i == second_answer - 1:
				second_cards = set([int(l) for l in line.split(' ')])

		matching_cards = first_cards.intersection(second_cards)
		if len(matching_cards) > 1:
			print 'Case #%d: %s' % (case_count, 'Bad magician!')
		elif len(matching_cards) == 1:
			print 'Case #%d: %d' % (case_count, matching_cards.pop())
		else:
			print 'Case #%d: %s' % (case_count, 'Volunteer cheated!')

		input_count -= 1
		case_count += 1


if __name__ == "__main__" : main()