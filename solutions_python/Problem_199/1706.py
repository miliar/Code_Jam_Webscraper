def flip(s):
	flipD = {'-':'+','+':'-'}
	return [flipD[x] for x in s]
def pancake(s, k):
	s = [str(d) for d in s]
	flips = 0
	for i in range(len(s)-k+1):
		if s[i] == '-':
			s[i:i+k] = flip(s[i:i+k])
			flips += 1
	if s.count('-') == 0:
		return flips
	else:
		return "IMPOSSIBLE"

def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		s, k = raw_input().split(" ")
		k = int(k)
  		print "Case #{}: {}".format(i, pancake(s,k))
  	# check out .format's specification for more formatting options

main()