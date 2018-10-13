from string import *
import math

parity = True

def simplify(elts, target):
	global parity

	head = elts[0]
	elts = elts[1:]

	for index in range(len(elts)):	

		if ((head == target) and parity):
			return elts

		head = operate(head, elts[0])
		elts = elts[1:]

	return [] # fail

def crush(elts, target):

	head = '1'

	for index in range(len(elts)):	
		head = operate(head, elts[index])

	return ((head == target) and parity)

def operate(elt1, elt2):

	global parity
	#print "crunching...." + elt1 + "  " + elt2 +  ' ' + str(parity)
	if (elt1 == '1'):
		return elt2

	elif (elt1 == 'i' and elt2 == 'i'):
		parity = not parity
		return '1'

	elif (elt1 == 'i' and elt2 == 'j'):
		return 'k'

	elif (elt1 == 'i' and elt2 == 'k'):
		parity = not parity
		return 'j'

	elif (elt1 == 'j' and elt2 == 'i'):
		parity = not parity
		return 'k'

	elif (elt1 == 'j' and elt2 == 'j'):
		parity = not parity
		return '1'

	elif (elt1 == 'j' and elt2 == 'k'):
		return 'i'

	elif (elt1 == 'k'):
		if (elt2 == 'i'):
			return 'j'
		elif (elt2 == 'j'):
			parity = not parity
			return 'i'
		elif (elt2 == 'k'):
			parity = not parity
			return '1'

def read_words(filename):
    '''
    converts a file to a list
    '''
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("in.txt", 'r')
numcases = int(filename.readline().split()[0])

for case in range(numcases):

	parity = True
	
	inline = filename.readline().split()
	length = int(inline[0])
	reps = int(inline[1])

	stringy = filename.readline().rstrip('\n') * reps

	stringy = simplify(stringy, 'i')

	if not (stringy == []):
		stringy = simplify(stringy, 'j')

		if not (stringy == []):

			if (crush(stringy, 'k')):
				print "Case #" + str(case+1) + ": " + "YES"
				continue
				
	print "Case #" + str(case+1) + ": " + "NO"
