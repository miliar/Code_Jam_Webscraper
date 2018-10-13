import math
import random
import re

def all_perms(str):
	if len(str) <=1:
		yield str
	else:
		for perm in all_perms(str[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + str[0:1] + perm[i:]

def is_last(ss):
	temp = ss[:]
	temp.sort()
	temp.reverse()
	return temp == ss

if __name__ == '__main__':
	#in_filename = "B-small.in"
	#in_filename = "B-dummy.in"
	in_filename = "B-large.in"
	#out_filename = "B-small.out"
	out_filename = "B-large.out"
	
	in_file = open(in_filename, 'r')
	out_file = open(out_filename, 'w')

	num_cases  = int(in_file.readline())

	for c in range(0,num_cases):
		num = in_file.readline()
		s = [int(x) for x in list(num)[:-1]]
		s.reverse()
		last = s[0]
		pos = -1
		for p in range(1,len(s)):
			if s[p] < last:
				pos = p
				break
			last = s[p]
				
		if pos != -1:
			#print "break",  s[pos]
			part = s[:pos]
			#print "part", part
			m = min(filter(lambda x: x > s[pos], part))
			#print "min",m
			ind = part.index(m)
			s[pos],s[ind] = s[ind],s[pos]
			part = s[:pos]
			part.sort()
			part.reverse()
			s = part + s[pos:]
		else:
			s.sort()
			s = s[:1] + [0] + s[1:]
			for i in range(0,len(s)):
				if s[i] != 0:
					s[0],s[i] = s[i],s[0]
					break
			
			s.reverse()
		s.reverse()
		ans = ''.join([str(x) for x in s])
		print ans
		out_file.write("Case #%d: %s\n" % (c+1, ans))

	out_file.close()

