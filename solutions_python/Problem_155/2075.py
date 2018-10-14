#Google Code Jam 2015 Problem A: Standing Ovation
#Joe Hallahan jphinspace@gmail.com
#10 Apr 2015

def friend_count(input):
	crowd_data = input.split(" ")
	s_max = int(crowd_data[0])
	crowd = map(int, list(crowd_data[1].rstrip()))
	friends = 0
	clapping = 0
	for i in range(len(crowd)):
		if clapping < i:
			friends += 1
			clapping += 1
		clapping += crowd[i]
	return friends

audience_file = open("A-large.in", "r")

test_case_count = int(audience_file.readline())
for i in range(test_case_count):
	print "Case #" + str(i+1) + ": " + str(friend_count(audience_file.readline()))

audience_file.close()
