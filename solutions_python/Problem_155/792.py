import fileinput
import sys


def ex1(line):
	people = line.split(" ")[1]
	standing = int(people[0])
	undecided = [int(x) for x in people[1:]]
	friends = 0
	for i in range(0, len(undecided)):
		# print "round %d" %i
		# print "standing %d" %standing
		# print "friends %d" %friends
		# print "undecided %d" %undecided[i]
		# print ""
		if undecided[i] > 0 and standing < i+1:
			friends_to_add = i+1 - standing
			standing += friends_to_add
			friends += friends_to_add
		standing += undecided[i]
	return friends


if __name__ == '__main__':
	i = 0
	for line in sys.stdin:
		if i > 0:
			print "Case #{0}: {1}".format(i, ex1(line.rstrip()))
		i += 1
    	
