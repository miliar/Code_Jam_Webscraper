amount = int(raw_input())
for a in range(amount):
	need_to_invite = 0
	going = 0
	string = raw_input().split(' ')
	for x in range(int(string[0]) + 1):
		if(going < x and string[1][x] !='0'):
			need_to_invite += x - going
			going += x - going
		going += int(string[1][x])
	print "Case #"+ str(a + 1) + ": " + str(need_to_invite)