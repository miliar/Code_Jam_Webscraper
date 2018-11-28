def solve(st):
	standing = 0
	invites = 0
	Smax, st = st.split()
	Smax = int(Smax)
	for i in xrange(Smax + 1):
		if standing >= i:
			standing += int(st[i])
		else:
			need_to_invite = i - standing # >0
		 	standing = standing + int(st[i]) + need_to_invite
		 	invites = invites + need_to_invite
		#print standing, invites
	return invites


t = input()

for i in xrange(t):
	s = raw_input()
	print("Case #" + str(i+1) + ": " + str(solve(s)))