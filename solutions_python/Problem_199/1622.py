  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys

def runtest(case, k):
	s = [x for x in case]
	count = 0
	for i in range(0,len(s)-(k-1)):
		if s[i]=='-':
			count+=1
			for m in range(k):
				s[i+m]= '+' if s[i+m] == '-' else '-'
	for x in s[i+1:]:
		if x=='-':
			return -1

	return count

f_dir = sys.argv[1]
fo_dir = sys.argv[2]

f = open(f_dir,'r')
fo = open(fo_dir,'w')

t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
  # n, m = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
  t = f.readline()[:-1].split(' ')
  ans = runtest(t[0],int(t[1]))
  fo.write("Case #"+str(i)+': '+(str(ans) if ans!=-1 else 'IMPOSSIBLE')+'\n')

f.close()
fo.close()