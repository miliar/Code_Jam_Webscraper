from sys import stdin,stdout
t = int(stdin.readline())
for tc in range(t):
	s = stdin.readline().strip()
	start = 0
	op = ''
	found = 0
	for i in range(len(s)-1):
		#get the decreasing part
		if s[i] > s[i+1]:
			#flip all from start
			#print "Start",start
			if int(s[start]) > 1:
				op += str(int(s[start]) - 1)
			op += '9'*(len(s) - (start+1))
			found = 1
			break
		elif s[i] < s[i+1]:
			op += s[start:i+1]
			start = i+1
		
	if found==0:
		op = s
	print "Case #{}: {}".format(tc+1,op)
			