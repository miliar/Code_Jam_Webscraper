#!/usr/bin/python

def is_sorted(l):
	if(l==sorted(l)):
		return True
	return False

def solve(n):

	l = list(str(n))
	last = int(l[0])
	index = 0
	s = str(n)
	t = ""

	for i in range(1,len(l)):

		current = int(l[i])

		if(current<last):
			t = s[i:]
			break

		last = current

	
	if(t==""):
		return n
	else:
		if(is_sorted(list(str(n)))):
			return n-(int(t)+1)
		else:
			return solve(n-(int(t)+1))


if __name__ == '__main__':
	t = int(raw_input())

	for i in xrange(1, t + 1):

	  n = int(raw_input())

	  result = solve(n)

	  x = str(i)
	  y = str(result)

	  print "Case #{}: {}".format(x,y)