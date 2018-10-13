def standingOvation(case, n, s):
	
	aud = 0
	friends = 0
	
	for i in range(len(s)):
		if i == 0:
			aud += int(s[i])
			continue
		elif aud < i:
			friends += 1
			aud += 1
			aud += int(s[i])
		else:
			aud += int(s[i])
	#print aud
	
	print "Case #" + str(case) + ": " + str(friends)
	
	
inp = raw_input()
T = int(inp)

for i in range(T):
	new_inp = raw_input().split()
	standingOvation(i+1, int(new_inp[0]), new_inp[1])
#standingOvation(4, '11111')
#standingOvation(1, '09')
#standingOvation(5, '110011')
#standingOvation(0, '1')