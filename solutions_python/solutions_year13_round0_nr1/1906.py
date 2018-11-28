import math

flist = []

def isPalindrome(n):
	n = str(n)
	length = len(n)
	#print length
	isPal = True
	for i in range(0,length/2):
		#print i
		#print n[i],n[length-i-1]
		if(n[i] != n[length-i-1]):
			isPal = False
			break
	#if(isPal): flist.append(n)
	return isPal

ffile = open('2.txt', 'w')
n = raw_input()
n = int(n)
for i in range(0,n):
	data = []
	for j in range(0,4):
		data.append(raw_input())
	raw_input()
	'''
	for k in range(0,4):
		for m in range(0,4):
			print data[k][m]
	'''
	out = ''
	complete = True

	# check horizontal and completion
	for j in range(0,4):
		# check complete
		if (data[j].count('.') > 0):
			complete = False
			#out = 'Case #'+str(i+1)+': Game has not completed'
		if (data[j].count('O') == 3 and data[j].count('T') > 0) or (data[j].count('O') == 4):
			out = 'Case #'+str(i+1)+': O won'
			break
		elif (data[j].count('X') == 3 and data[j].count('T') > 0) or (data[j].count('X') == 4):
			out = 'Case #'+str(i+1)+': X won'
			break

	#check vertical
	for j in range(0,4):
		if (out):
			break
		checkstr = data[0][j]+data[1][j]+data[2][j]+data[3][j]
		#print checkstr
		if (checkstr.count('O') == 3 and checkstr.count('T') > 0) or (checkstr.count('O') == 4):
			out = 'Case #'+str(i+1)+': O won'
			break
		elif (checkstr.count('X') == 3 and checkstr.count('T') > 0) or (checkstr.count('X') == 4):
			out = 'Case #'+str(i+1)+': X won'
			break

	#check diagonal left
	if (not out):
		checkstr = data[0][0]+data[1][1]+data[2][2]+data[3][3]
		#print '>>',checkstr
		if (checkstr.count('O') == 3 and checkstr.count('T') > 0) or (checkstr.count('O') == 4):
			out = 'Case #'+str(i+1)+': O won'
		elif (checkstr.count('X') == 3 and checkstr.count('T') > 0) or (checkstr.count('X') == 4):
			out = 'Case #'+str(i+1)+': X won'

	#check diagonal right
	if (not out):
		checkstr = data[0][3]+data[1][2]+data[2][1]+data[3][0]
		#print '>>',checkstr
		if (checkstr.count('O') == 3 and checkstr.count('T') > 0) or (checkstr.count('O') == 4):
			out = 'Case #'+str(i+1)+': O won'
		elif (checkstr.count('X') == 3 and checkstr.count('T') > 0) or (checkstr.count('X') == 4):
			out = 'Case #'+str(i+1)+': X won'

	#no one wins
	if (not complete) and (not out):
		out = 'Case #'+str(i+1)+': Game has not completed'
	elif (complete) and (not out):
		out = 'Case #'+str(i+1)+': Draw'


	#out = 'Case #'+str(i+1)+': '+str(count)
	#print out
	ffile.write(out+'\n')