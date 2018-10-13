#!/usr/bin/pythonw
def isTidy(n):
	number_string = str(n)
	if(len(number_string)==1):
		return True
	for j in xrange(1,len(number_string)):
		if(number_string[j]<number_string[j-1]):
			return False
	return True
def tidy(n):
	number_string = list(str(n))
	for j in xrange(1,len(number_string)):
		if(number_string[j]<number_string[j-1]):
			if(number_string[j]==0 and j==len(number_string)):
				del(number_string[-1])
				break
			else:
				for r in xrange(j,len(number_string)):
					number_string[r] = '9'
				number_string[j-1] = str(int(number_string[j-1]) - 1)
				break
	return int("".join(number_string))
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  while not(isTidy(n)):
  	n = tidy(n)
  print "Case #{}: {}".format(i, n)
  # check out .format's specification for more formatting options