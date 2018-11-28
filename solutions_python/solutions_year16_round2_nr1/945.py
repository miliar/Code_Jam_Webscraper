import sys

"""
(Z)ERO
EI(G)HT
T(W)O
SI(X)
(S)EVEN
(T)HREE
FI(V)E
N(I)NE
(F)OUR
ONE
"""

def get_index(character):
	return ord(character)- ord('A')

def get_histogram(message):
	histo = [0 for i in range(27)]
	for c in message:
		histo[get_index(c)] += 1
	return histo

def digit_number(message):
	priority_list = [0,8,2,6,7,3,5,9,4,1]
	english_d = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	unique_char = {0 : 'Z', 8 : 'G', 2 : 'W', 6: 'X', 7: 'S', 3: 'T', 5: 'V', 9: 'I', 4: 'F', 1:'O'}
	histogram = get_histogram(message)
	digit_occurences =  [0 for i in range(10)]
	for current_digit in priority_list:
		nb_current_digit =  histogram[get_index(unique_char[current_digit])]
		digit_occurences[current_digit] = nb_current_digit
		for c in english_d[current_digit]:
			histogram[get_index(c)] -= nb_current_digit
	return digit_occurences

def get_phone_number(message):
	digit_num = digit_number(message)
	phone_number = ""
	for i in range(10):
		for _ in range(digit_num[i]):
			phone_number += str(i)
	return phone_number


def main():
	t = int(sys.stdin.readline().strip())
	for i in range(1,t+1):
		message = sys.stdin.readline().strip()
		digit_num = digit_number(message)
		print "Case #%d: %s" % (i, get_phone_number(message))

if __name__ == '__main__':
	main()