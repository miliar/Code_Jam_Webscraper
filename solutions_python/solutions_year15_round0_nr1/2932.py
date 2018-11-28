t = raw_input()
tot = 0
add = 0
pep = 0
for i in range(0, int(t)):
	case = raw_input()
	s_str = case.split(' ')
	smax = int(s_str[0])
	string = s_str[1]
	for x in range(0, len(string) - 1):
		tot += int(string[x])
		pep += int(string[x])
		if(pep > smax):
			break
		if(tot < (x + 1)):
			add += (x + 1) - tot
			tot += 1
	print "Case #" + str(i+1) + ": " + str(add)
	tot = 0
	add = 0
	pep = 0

