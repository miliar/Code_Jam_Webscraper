import string

def testLine(n):
	first = file.readline()
	second = file.readline()
	firstBlankIndex = string.find(first," ")
	
	secondBlankIndex = string.find(first," ",firstBlankIndex+1)
	R = int(first[0:firstBlankIndex])
	K = int(first[firstBlankIndex+1:secondBlankIndex])
	N = int(first[secondBlankIndex+1:-1])
	Queue = []
	b=""	
	counter=0
	while counter<len(second):
		if second[counter] !=" ":
			b+=second[counter]
			
		else:
			Queue+=[int(b),]
			b=""
		counter+=1
	Queue+=[int(b),]
#	print R,K,N
#	print Queue
	currentVolume=0
	currentIndex=0
	totalVolume = 0
	
	for ride in range(1,R+1):
		counter=0
		while currentVolume + Queue[currentIndex]<=K and counter<len(Queue):
			currentVolume+=Queue[currentIndex]
			currentIndex=(currentIndex+1)%N
			counter+=1
		totalVolume+=currentVolume
		currentVolume = 0
	output.write("Case #"+str(n)+": "+str(totalVolume)+"\n")

file = open("C-small-attempt3.in","r")
output = open("output3.txt","w")
counter = int(file.readline())
for i in range(1,counter+1):
	testLine(i)