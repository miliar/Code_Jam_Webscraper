readFile = open("B-large.in")
testCases = eval(readFile.readline())

ans = {}
for t in range(0,testCases):
    number = str(eval(readFile.readline()))

    if len(number) == 1:
	ans[t] = int(number)
    else:
	#equal occurences of number
	index = 0
	valid = True
    	#check if all digits are in increasing order
    	for i in range(1,len(number)):
	    if int(number[i]) < int(number[i-1]):
		index = i-1
		valid = False
	    	break
	if valid:
	   ans[t] = int(number)
	else:
	   sIndex = 0
	   #check how many numbers before index are same
	   for i in range(index,0,-1):
	        if int(number[i]) != int(number[i-1]):
		    sIndex = i
		    break

	   n = int(number[sIndex])-1
	   ni = '' if n==0 else str(n)
	   temp = number[:sIndex]+ni+'9'*(len(number)-sIndex-1)
	   ans[t] = temp

outputFile = open("Tidy_Numbers_Output_Large.txt",'w')
for i in range(0,len(ans)):
    outputFile.write("Case #%d: %s\n" % (i+1,ans[i]))

	

