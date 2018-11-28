



def main():

	numOfcases = int(input())

	output = []

	for i in range(numOfcases):
		case = input()
		while not isGood(case):
			case = int(case)
			case -= 1
			case = str(case)

		output.append("Case #"+ str(i+1)+ ": "+case)

	for out in output:
		print(out)



def isGood(stringCase):

	good = True	

	for charIndex in range(len(stringCase)-1, 0, -1):
		if int(stringCase[charIndex]) < int(stringCase[charIndex-1]):
			good = False

	return good
					

main()

'''
def main():

	numOfcases = int(input())

	output = []

	for i in range(numOfcases):
		case = input()
		good = isGood(case)[0]
		case = isGood(case)[1]
		while not good:
			good = isGood(case)[0]
			case = isGood(case)[1]

		output.append("Case #"+ str(i)+ ": "+case)

	for out in output:
		print(out)



def isGood(stringCase):

	good = True 	

	for charIndex in range(len(stringCase)-1, 0, -1):
		if int(stringCase[charIndex]) < int(stringCase[charIndex-1]):
			stringCase = str( int(stringCase) - (int(stringCase[charIndex-1]) -int(stringCase[charIndex]) ) )
			good = False

	return [good,stringCase]
'''