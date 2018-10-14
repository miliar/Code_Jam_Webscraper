
def isCons(a):
	if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
		return False
	else:
		return True	


def largestContinuousSum(arr):
    if len(arr)==0:
        return
    maxSum=currentSum=arr[0]
    for num in arr[1:]:
        currentSum=max(currentSum+num, num)
        maxSum=max(currentSum, maxSum)
    return maxSum
    
    
def convArr(arr):
	num=[]
	i=0
	while i<len(arr):
		if(isCons(arr[i])):
			num.append(1)
		else:
			num.append(-200)
			
		i = i+1		
	
	return num
	    

tc=input()
casei=1

while casei<=tc:
	count=0
	
	line = raw_input()
	word=line.split(" ")[0]
	n=int(line.split(" ")[1])
	
	length = len(word)
	start = 0
	while start<length:
		
		end = start + n
		while end<=length:
			
			#print start,end,word[start:end]
			numarr = convArr(word[start:end])
			if largestContinuousSum(numarr)>=n:
				count = count+1
			
			end = end +1
		
		start = start +1
	
	
	
	#numarr = convArr(word)
	#print largestContinuousSum(numarr)
	
	#print count
	
	print "Case #"+str(casei)+": "+str(count)
	casei = casei+1
	
	
	
	
	
	
	
	
	
	
	
	
