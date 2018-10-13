import fileinput
import sys, getopt

def solve2(S_max, slist):
	friendsNeeded = 0
	totalSoFar = 0

	for i in range(S_max + 1):
		temp_total = totalSoFar + friendsNeeded
		if temp_total < i:
			friendsNeeded = friendsNeeded + (i - temp_total)
		totalSoFar = totalSoFar + int(slist[i])

	return friendsNeeded


def main(args):
	filename = args[0]
	case_num = 1
	for line in fileinput.input(filename):
		if not fileinput.isfirstline():
			case = line.rstrip('\n').split(' ')
			res = solve2(int(case[0]),list(case[1]))
			print 'Case #' + str(case_num) + ': ' + str(res)
			case_num = case_num + 1


if __name__ == "__main__":
	main(sys.argv[1:]);