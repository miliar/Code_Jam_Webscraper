f = open('input.txt', 'r')

cases = int(f.readline())

count = 0
casenum = 1
line1 = -1
line2 = -2
str1 = []
str2 = []

for line in f:
	if casenum <= cases:
		if(count == 0):
			line1 = int(line)
		elif(count == line1):
			str1 = line.rstrip().split(' ')
		elif count == 5:
			line2 = int(line) + 5
		elif count == line2:
			str2 = line.rstrip().split(' ')
			c = 0
			ans = 0
			for x in str1:
				if x in str2:
					c += 1
					ans = x
			if c == 1:
				print "Case #{casenum}: {ans}".format(casenum=casenum, ans=ans)
			elif c == 0:
				print "Case #{casenum}: {ans}".format(casenum=casenum, ans="Volunteer cheated!")
			else:
				print "Case #{casenum}: {ans}".format(casenum=casenum, ans="Bad magician!")
		if count == 9:
			count = 0
			casenum += 1
		else:
			count += 1
	else:
		break
