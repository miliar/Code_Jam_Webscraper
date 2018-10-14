def getAB(string):
	list = string.split()
	return (int(list[0]), int(list[1]))

def calculateRecycled(string):
	A,B = getAB(string)
	pairs = {}
	for num in range(A,B+1):
		original = str(num)
		for digits in range(1,len(original)):			
			newNum = (original[-digits:]+original[:len(original)-digits])
			intNum = int(newNum)
			if intNum >= A and intNum <=B and len(newNum) == len(original) and intNum != num:
				if (num < intNum):
					if num in pairs.keys():
						if intNum not in pairs[num]:
							pairs[num].append(intNum)
					else:
						pairs[num] = [intNum]
#	print pairs
	count = 0
	for key in pairs.keys():
		#print key,": ", pairs[key]
		count = count + len(pairs[key])
	return count
	

#lowest number is going to be sort(num) => 51234 => 12345
#highest number is going to be sort(num), switch last => 51234
	
if __name__ == "__main__":
	import sys
	file = open(sys.argv[1],'r')
	numTests = file.readline()
	for case in range(int(numTests)):
		string = "Case #"+str(case+1)+": "+str(calculateRecycled(file.readline()))
		string = string.rstrip()
		string = string.lstrip()
		print string
		
		