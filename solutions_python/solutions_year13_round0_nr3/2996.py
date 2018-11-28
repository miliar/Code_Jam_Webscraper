
def isPoli(y):
	s = str(y)
	for i in range (0,len(s)/2):
		if s[i]!=s[len(s)-1]:
			return False
	return True

all = range(1,1000)
fromNums = [x for x in all if isPoli(x)]
#print fromNums
#fromNums = [1,2,3,4,5,6,7,8,9,11,22,33]

sqredNums = [x**2 for x in fromNums]
#print sqredNums

output = [y for y in sqredNums if isPoli(y)]
#print output


inpFile = open("int.txt","r")

NumCases = int(inpFile.readline())

for m in range (0,NumCases):
	nums = inpFile.readline().split(" ")
	numA = int(nums[0])
	numB = int(nums[1])
	outs = [x for x in output if x<=numB and x>=numA]
	#print outs
	print "Case #"+str(m+1)+": "+str(len(outs))
