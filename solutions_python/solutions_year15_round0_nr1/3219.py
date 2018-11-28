import sys

def solve():
	ts = sys.stdin.readline()
	for t in xrange(int(ts)):
		line = sys.stdin.readline().split()
		s_max = line[0]
		s = line[1]
	
		need_friends = 0
		people_counter = 0 
		for i in xrange(1, len(s)+1):
			if people_counter > s_max:
				break
			if s[i-1] == '0':
				if people_counter < i:
					need_friends += i - people_counter 
					people_counter += 1
			else:
				people_counter += int(s[i-1])
		
		print "Case #{0}: {1}".format(t+1, need_friends)		

solve()


