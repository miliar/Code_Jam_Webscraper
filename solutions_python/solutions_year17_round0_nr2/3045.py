# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	numberArray = raw_input().split()	#limitNumber is highest number received
	limitNumber = numberArray[0]
	indexToDrop = 0
	for num in range(0, len(limitNumber)):
		newNum = limitNumber[num]
		if limitNumber[indexToDrop] < newNum:
			indexToDrop = num
		elif limitNumber[indexToDrop] > newNum:
			#must drop by 1 and convert to 9's
			limitNumber = limitNumber[:indexToDrop] + str(int(limitNumber[indexToDrop]) - 1) + limitNumber[indexToDrop +1:]
			for replaceToNine in range(indexToDrop+1, len(limitNumber)):
				limitNumber = limitNumber[:replaceToNine] + '9' + limitNumber[replaceToNine +1:]
			break
		else:
			#do nothing, move to next
			continue
	if limitNumber[0] == '0':
		limitNumber = limitNumber[1:]
	print("Case #" +str(i) +": " + limitNumber)
  #print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options