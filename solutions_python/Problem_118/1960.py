import math

def palindrome(word):
	return word == word[::-1]

def main(file):
	inputfile = open(file, 'r')
	howmany = int(inputfile.readline()) # how many test cases are there?
	stage = 0

	outputfile = open('C-small-attempt1.out', 'wd')
	
	while stage < howmany:
		word = inputfile.readline().split()
		s,f = int(word[0]),int(word[1])+1 #starting and finishing integer for the interval
		count = 0
		for squrenumber in range(s,f):
			if palindrome(str(squrenumber)):
				if math.sqrt(squrenumber).is_integer():
					if palindrome(str(int(math.sqrt(squrenumber)))):
						count += 1

		stage += 1
		msg = "Case #" + str(stage) + ": " + str(count) + "\n"

		outputfile.write(msg)









if __name__ == '__main__':
	main('C-small-attempt1.in')





















