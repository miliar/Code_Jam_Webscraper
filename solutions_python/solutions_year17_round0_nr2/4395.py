test_case = raw_input()
ans = []
for i in range(1,int(test_case)+1):
	num = list(raw_input())
	for num_i in xrange(1,len(num)+1):
		if num_i == len(num):
			continue
		if int(num[len(num)-num_i]) < int(num[len(num)-num_i-1]):
			num[len(num)-num_i-1] = str(int(num[len(num)-num_i-1])-1)
			for nine in xrange(len(num)-num_i,len(num)):
				num[nine] = "9"
	ans.append(str(int("".join(num))))
for i in range(1,int(test_case)+1):
	print "Case #"+str(i)+": "+ans[i-1]