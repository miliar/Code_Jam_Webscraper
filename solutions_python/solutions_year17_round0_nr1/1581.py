#!/usr/bin/python


def solve(s, k):
	times = 0
	for i, j  in enumerate(s):
		if(j==-1):
			if(i+k<=len(s)):
				for p in range(i,i+k):
					s[p] *= -1
				times+=1
	

	if(-1 in s):
		return "IMPOSSIBLE"
	return times




if __name__ == '__main__':
	t = int(raw_input())

	for i in xrange(1, t + 1):

	  s,k = raw_input().split(" ")

	  k = int(k)
	  p = []

	  for ss in s:
	  	if(ss == '+'):
	  		p.append(1)
	  	else:
	  		p.append(-1)

	  result = solve(p,k)

	  x = str(i)
	  y = str(result)

	  print "Case #{}: {}".format(x,y)