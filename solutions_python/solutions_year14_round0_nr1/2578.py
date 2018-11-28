#!/usr/bin/env python
import sys

def main():
	# Setup input and output file handlers
	if len(sys.argv) == 1:
		f_in = sys.stdin
		f_out = sys.stdout
	else:
		f_in = open(sys.argv[1])
		if len(sys.argv) > 2:
			f_out = open(sys.argv[2], 'w')
		else:
			f_out = sys.stdout

	# Code here
	T = int(f_in.readline())
	for t in range(T):
		f_out.write('Case #%d: ' % (t+1))
		ans = int(f_in.readline())
		cards = []
		for i in range(4):
			cards.append(list(map(int, f_in.readline().split(' '))))

		options = cards[ans - 1]

		ans = int(f_in.readline())
		cards = []
		for i in range(4):
			cards.append(list(map(int, f_in.readline().split(' '))))
		
		answers = []

		for card in cards[ans-1]:
			if card in options:
				answers.append(card)

		if len(answers) > 1:
			f_out.write('Bad magician!')
		elif len(answers) == 0:
			f_out.write('Volunteer cheated!')
		else:
			f_out.write(str(answers[0]))
			
		f_out.write('\n')

	f_in.close()
	f_out.close()

if __name__=='__main__':
	main()
