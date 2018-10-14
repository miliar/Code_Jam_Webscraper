T = int(raw_input(''))
cases = []
for i in range(T):
 case = raw_input('')
 cases = cases + [case]
for i in range(T):
	case = cases[i]	
	standing = int(case[2])
	friend = 0
	for k in range(len(case)-3):		
		if int(k + 1) > standing:
			while int(k + 1) > standing:
				friend = friend + 1
				standing = standing +1
			standing = standing + int(case[k +3])
		else:
			standing = standing + int(case[k + 3])
	print 'Case #'+str(i+1)+': ' + str(friend)