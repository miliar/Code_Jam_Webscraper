with open('A-large.in', 'r') as f:
	content = f.readlines()
	content = [x.strip('\n') for x in content]
	# print "content: ",content
f.close()

cases = int(content[0])
f = open('A-large-output','w')

for i in range(0, cases):
	ans = 0
	string = content[i+1]
	string = string.split(' ')[1]
	l = len(string)
	sum1 = 0
	for k in range(0, l):
		if sum1 < k:
			ans += k-sum1
			sum1+= k-sum1
		sum1 += int(string[k])
	ans_string = "Case #"+str(i+1)+": "+str(ans)
	f.write(ans_string+"\n")

f.close()