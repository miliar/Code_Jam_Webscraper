import sys

tests_count = int(sys.stdin.readline())

for k in xrange(tests_count):
	S_max, s = sys.stdin.readline().split(" ")
	S_max = int (S_max)

	curr_person = 0
	needed = 0

	for i in xrange(S_max+1):
		curr_s = int(s[i])
	 	if (curr_person < i):
			needed += i - curr_person
			curr_person += i - curr_person
		curr_person += curr_s
	
	print "Case #{}: {}".format(k+1, needed)
	