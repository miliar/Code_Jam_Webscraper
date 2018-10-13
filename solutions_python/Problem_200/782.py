def exe2(list1):
	flag=0	
	for i in xrange(len(list1)-1,0,-1):
		for j in xrange(i-1,-1,-1):
			if int(list1[j])>int(list1[i]):
				list1[j]=str(int(list1[j])-1)
				for k in xrange(j+1,len(list1)):
					list1[k]='9'
				break
	string=""
	for s in list1:
		if  flag!=0:
			string= string + str(s)	
		else:
			if s!='0':
				string= string + str(s)	
				flag=1
	return string


import time
start = time.time()
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [str(s) for s in raw_input()]
  print "Case #{}: {}".format(i, exe2(list(n)))
  # check out .format's specification for more formatting options
end = time.time()
#print(end - start)
