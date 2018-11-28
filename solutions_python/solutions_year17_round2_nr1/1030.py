num= int( input() )
#a, b= input.split(" ")
#arr= [int(x) for x in input().spilt(" ")]

def clash(horse1Loc, horse2Loc, horse1Sped, horse2Sped, dist):
	#horse 1 is the index of the horse that is to the left
	time1= (dist- horse1Loc)/ horse1Sped
	time2= (dist-horse2Loc)/horse2Sped
	if time1< time2:
		return True
	else:
		return False

def calcTime(horseLoc, dist, speed):
	return (dist-horseLoc) /speed

def findLastHorse(indHorse):
	if indHorse== n-1:
		return calcTime(locArr[indHorse], d, speedArr[indHorse])
	else:
		for i in range(indHorse+1, n):
			if clash(locArr[indHorse], locArr[i], speedArr[indHorse], speedArr[i], d):
				return findLastHorse(i)
		return calcTime(locArr[indHorse], d, speedArr[indHorse])



for i in range(1, num+1):
	d , n=input().split(" ")#int(input())
	d= int(d)
	n= int(n)
	#n =int(input())
	locArr=[]
	speedArr=[]
	for j in range(n):
		k, s = [int(x) for x in input().split(" ")]
		#temp.append(int(input()))
		locArr.append(k)
		speedArr.append(s)
	time= findLastHorse(0)

	result= d/time 


	print( "Case #{}: {}".format(i, result) )