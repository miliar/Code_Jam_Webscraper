import sys

def challenge(input):
	shyness = list(input.strip('\n'))[2:]
	totalApplause = 0
	newFriends = 0
	for i in xrange(len(shyness)):
		if(i is 0):
			totalApplause = int(shyness[i])
			continue
		if(totalApplause < i):
			while(totalApplause < i):
				newFriends = newFriends + 1
				totalApplause = totalApplause + 1
		totalApplause = totalApplause + (int(shyness[i]))
	return newFriends
		

def main(lines):
	case = 0
	for line in lines:
		if(case is 0):
			case = case + 1
			continue
		print('Case #' + str(case) + ': ' + str(challenge(line)))
		case = case + 1

if __name__ == "__main__":
	main(sys.stdin.readlines())