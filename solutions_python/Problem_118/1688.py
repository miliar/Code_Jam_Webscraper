def nextPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftHalf(num)
    middle=getMiddle(num)
    if oddDigits:
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
    if newNum>num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextPalindrome(roundUp(num))
 
def getLeftHalf(num):
    return str(num)[:len(str(num))/2]
 
def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment



def checkPalindrome(num2):
	i=0; pal=1;
	num = str(num2)
	length = len(num)
	while i<length/2 and pal ==1:
		if(num[i] <> num[length -i -1]):
			pal=0
		i = i +1

	if pal == 1:
		return 1
	else:
		return 0

	

tc=input()
casei=1

while casei<=tc:

	count=0
	line = raw_input()
	start=int(line.split(" ")[0])
	end=int(line.split(" ")[1])
	#end=522808225;
	initial = int(pow(start,0.5))-1

	proceed=1 

	nextPal = nextPalindrome(initial)
	sqrPal = pow(nextPal,2)



	

	while sqrPal <= end and proceed==1:
		#print str(sqrPal) 
		#print str(nextPal)
		if sqrPal < start:
			dummy=0
		else:
			if checkPalindrome(sqrPal):
				count = count + 1
		if sqrPal==end:
			proceed = 0

		if proceed==1:
			nextPal = nextPalindrome(nextPal)
			sqrPal = pow(nextPal,2)


	print "Case #"+str(casei)+": "+str(count)


	casei = casei + 1











