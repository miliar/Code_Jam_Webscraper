from string import *
import math

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
	inline = filename.readline().split()
	maxshy = int(inline[0])
	shyrray = inline[1:]

	numstanding = 0;
	friends = 0;

	for index in range(maxshy+1):
		if (int(shyrray[0][index]) == 0):
			continue
		else:
			if (numstanding >= index):
				numstanding += int(shyrray[0][index])
			else:
				while (numstanding < index):

					friends +=1
					numstanding+=1

				numstanding += int(shyrray[0][index])

	print "Case #" + str(case+1) + ": " + str(friends)

