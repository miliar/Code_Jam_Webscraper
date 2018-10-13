def ispalindrome(x):
	string = str(x)
	palindromelen =len(string)
	if palindromelen==1:
		return 1
	palindromelen /= 2
	return string[:palindromelen]==string[-palindromelen:][::-1]

t = int(raw_input());
for testcase in range(1,t+1):
	string = raw_input()
	(start,end) = string.split()
	start = int(start)
	end = int(end)
	ans = 0
	now = int(start**(0.5))
	while 1!=0:
		NOW = now * now
		if NOW > end:
			break
		if NOW>=start and ispalindrome(now) and ispalindrome(NOW):
			ans+=1
		now+=1
	print("Case #"+str(testcase)+": "+str(ans))

