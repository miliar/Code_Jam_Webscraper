import lib
from sets import Set

@lib.wrapper
def solution(input, output):
	T = input.int()
	for case in xrange(1,T+1):
		cards = []
		for arr in range(2):
			row = input.int()
			for i in range(1,5):
				if i==row:
					cards.append(Set(input.int_list()))
				else:
					input.str()
		cut = cards[0] & cards[1]
		if len(cut)==0:
			output.result(case, "Volunteer cheated!")
		elif len(cut)==1:
			output.result(case, list(cut)[0])
		else:
			output.result(case, "Bad magician!")

if __name__ == '__main__':
	solution("A-small-attempt0.in", "A-small-attempt0.out")
