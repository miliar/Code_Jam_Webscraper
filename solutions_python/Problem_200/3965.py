DP = []


def is_tidy(n):
	prev = 10
	while n != 0:
		units = n%10
		if units <= prev:
			prev = units
			n = n/10
		else:
			return False
	return True

def create_DP(n):
	DP.append(-1)
	for i in xrange(1, n+1):
		if is_tidy(i):
			DP.append(i)
		else:
			DP.append(DP[i-1])

create_DP(1000)
T = int(raw_input())

for i in xrange(1, T+1):
	num = int(raw_input())
	print "Case #" + str(i) +": " + str(DP[num])
