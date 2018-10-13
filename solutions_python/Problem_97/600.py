#!/usr/bin/python3



def gen_recycled(n, B):
	"""
	Return all the recycled numbers associated that are greater than n
	"""
	
	txt = str(n)
	
	res = 0
	col = []
	for p in range(len(txt)):
		if txt[0]>txt[p]:
			continue
		
		m = int(txt[p:] + txt[0:p])
		if n<m<=B and not m in col:
			res += 1
			col.append(m)
	return res
	

def count_in_range(A,B):
	
	n = A
	res = 0
	while (n<B):
		res += gen_recycled(n, B)
		n += 1
	return res




	

import sys		
# Now read the input and decode it
if len(sys.argv)<2:
	fd = sys.stdin
else:
	fd = open(sys.argv[1],"r")

T = int(fd.readline().strip())
	
for i in range(T):
	
	A, B = [ int(x) for x in fd.readline().strip().split() ]
	print("Case #%d: %d" % (i+1, count_in_range(A,B)))

fd.close()


		
	
	
