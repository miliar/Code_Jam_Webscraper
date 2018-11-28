
#input
f = open('A-large.in', 'r')
o = open('out.txt', 'w')
t = int(f.readline())
print(t)

for j in range(t):
	inputStr = f.readline().split()[1]
	print(inputStr)

	friendsHired = 0
	standers     = 0

	count = 0
	for i in inputStr:
		shyLevel = count

		# determine if previous was empty
		prevEmpty = False
		if(count != 0):
			prevEmpty = int(inputStr[count -1]) < 1

		if not prevEmpty:
			standers = standers + int(i)
		elif str(i) != 0:
			newHires = 0
			if(shyLevel > standers):
				newHires = shyLevel - standers
			standers = standers + newHires + int(i)
			friendsHired = friendsHired + newHires


		count = count + 1




	o.write('Case #' + str(j + 1) + ': ' + str(friendsHired) + '\n')





