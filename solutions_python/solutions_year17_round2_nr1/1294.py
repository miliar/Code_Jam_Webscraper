
if __name__ == '__main__':

	caseNum = int(input())

	for k in range(caseNum):
		maxTime = 0
		dest, horseNum = [int(s) for s in input().split(" ")]
		for i in range(horseNum):
			position, speed = [int(s) for s in input().split(" ")]
			time = (dest-position)/speed
			if(time>maxTime):
				maxTime = time
		maxSpeed = dest/maxTime
		print("Case #{}: {}".format(k+1,maxSpeed))
