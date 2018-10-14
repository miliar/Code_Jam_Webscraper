  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys

def runtest(n,k):
	count = 0
	dic = {n:1}
	next_dic = {}
	for _ in range(k):
		# print(stack, next_stack)
		for num in list(sorted(dic.keys(),reverse=True)):
			if num%2 == 1:
				l,r = (num-1)/2, (num-1)/2
			else:
				l,r = num/2, num/2-1
			count+=dic[num]
			if count>=k:
				return l,r
			if l!=0:
				if l not in next_dic:
					next_dic[l]=dic[num]
				else:
					next_dic[l]+=dic[num]
			if r!=0:
				if r not in next_dic:
					next_dic[r]=dic[num]
				else:
					next_dic[r]+=dic[num]
		dic = next_dic
		next_dic = {}
			# stack.sort(reverse=True)
	return (l,r)


f_dir = sys.argv[1]
fo_dir = sys.argv[2]

f = open(f_dir,'r')
fo = open(fo_dir,'w')

t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
  # n, m = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
  t = f.readline()[:-1].split()
  l,r = runtest(int(t[0]),int(t[1]))
  fo.write("Case #"+str(i)+': '+ '%d %d'%(l,r) +'\n')

f.close()
fo.close()