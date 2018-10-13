
import math
import os



#matrix = [[INF for x in range(5)]for x in range(4)]

def main():
	
	f = open('small1.txt', 'r')
	
	myList = []

	for line in f:
		numTestcase = line[0]
		break

	for line in f:
		myList.append(line)

	counter = 1
	for l in myList:
		NumPeopleNeeded(l, counter)
		counter += 1

	f.close()
	return 0 


def NumPeopleNeeded(l, case):

	k = l.split(" ", 2)
	loop = int(k[0])
	numList = k[1]
	numPeople = 0
	numStanding = 0

	for x in range(0, loop + 1):
		i = int(numList[x])
		if(x == 0 and i != 0):
			numStanding += i
			continue
		if(numStanding < x and i != 0):
			numPeople += (x - numStanding)
			numStanding += numPeople + i
		else:
			numStanding += i

	print "Case #"+ str(case) + ": " + str(numPeople)
	return 0

if __name__ == '__main__':
	main()


