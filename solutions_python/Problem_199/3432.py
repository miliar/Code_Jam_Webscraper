def flipk(s):
	#print "flip k for s "+s
	news =''
	#print len(s)
	for c in s:
		if c == '-':
			news = news+'+'
		if c == '+':
			news = news +'-'
	#print "news "+str(news)
	#print "end flipk"
	return news

def solve_a_k(s, k, count):
	#print "in solve a with s:"+str(s)+" k: "+str(k)
	#base case:
	if len(s) == k:

		#print "base case s is same size as k"
		if s == '+'*k: # s is all +, no flip needed
			return count
		if s == '-'*k: # s is all -, one flip needed
			return count + 1
		else: #s is a mix of + and 1, no flip is possible
			return -1
	else:
		#print "len s bigger than k"
		if s[0] =='+':
			return solve_a_k(s[1:], k, count)
		if s[0] =='-':
			sk = flipk(s[0:k])
			s = sk + s[k:]
			#print ("s after flip first k "+str(s))
			return solve_a_k(s[1:], k, count+ 1)



def solve_a(s, k):
	ans = solve_a_k(s,k,0)
	if ans == -1:
		return "IMPOSSIBLE"
	else:
		return ans


#test1 = '---+-++- 3'
#test2 = '+++++ 4'
numcase = int(raw_input())
#for i in [1]:
for i in range(numcase):
	#case = test1#
	case = raw_input()
	
	s, k = case.split(" ")
	k = int(k)
	#print s
	ans = solve_a(s, k)
	
	print "Case #"+str(i+1)+": "+str(ans)
