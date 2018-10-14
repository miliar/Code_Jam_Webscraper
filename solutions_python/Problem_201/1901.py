def solve(input):
	def splitLargestSegment():
		#find largest segment
		largestIndex = findLargest()
		#split in two and reinsert
		newSegmentLeft = int((segments[largestIndex]-1)/2)
		if (segments[largestIndex]%2) != 0:
			#for odd numbers
			newSegmentRight = newSegmentLeft
		else:
			#even numbers
			newSegmentRight = newSegmentLeft+1

		#insert new segments
		segments[largestIndex] = newSegmentLeft
		segments.insert(largestIndex+1, newSegmentRight)

	def findLargest():
		largestIndex = 0
		for i in range(len(segments)):
			if segments[i] > segments[largestIndex]:
				largestIndex = i
		return largestIndex

	data = input.split(" ")
	N = int(data[0])
	K = int(data[1])

	segments = [N]
	#whenever a toileteer arrives:
	for i in range(K-1):
		splitLargestSegment()
	#final toileteer
	largestIndex = findLargest()
	maximum = int(segments[largestIndex]/2)

	if segments[largestIndex]%2 == 0:
		#even spaces
		minimum = maximum-1
	else:
		minimum = maximum
	return str(maximum)+" "+str(minimum)

T = int(input())  # reads in number of test cases

# Take input
for i in range(1, T + 1):
    print("Case #{}: {} ".format(i, solve((input()))))