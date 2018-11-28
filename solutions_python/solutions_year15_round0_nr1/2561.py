import sys
input_str = "4\n4 11111\n1 09\n5 110011\n0 1"
if len(sys.argv) >= 2:
	input_str = file(sys.argv[1]).read()
spl = input_str.split('\n')
case_n = int(spl[0])
for casei in range(1, case_n+1):
	splspl = spl[casei].split(' ')
	maxfriends = int(splspl[0])
	max_clapping_nonfriend = 0
	case_friend_n = 0
	for friends in range(0, maxfriends+1):
		clapping = friends
		for i in range(0, maxfriends+1):
			if (clapping >= i):
				clapping += int(splspl[1][i])
		if (clapping - friends > max_clapping_nonfriend):
			max_clapping_nonfriend = clapping - friends
			case_friend_n = friends
	print "Case #" + str(casei) + ": " + str(case_friend_n)
