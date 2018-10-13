def findFirstLower(number):
	for i in range(1, len(number)):
		prev = number[i-1]
		curr = number[i]
		if curr < prev:
			return i-1
	return -1

def backTrack(number, idx):
	val = number[idx]
	for i in range(idx)[::-1]:
		if number[i] < val:
			return i+1
	return 0

def swapNines(number, idx):
	nineCount = len(number)-idx-1
	newNumber = number[:idx] + [number[idx]-1] + [9]*nineCount
	return newNumber

def findLargestTidy(number):
	numList = [int(c) for c in number]
	decrIdx = findFirstLower(numList)
	if decrIdx < 0:
		return number
	decrIdx = backTrack(numList, decrIdx)
	numList = swapNines(numList, decrIdx)
	if numList[0] == 0:
		return "".join([str(x) for x in numList[1:]])
	return "".join([str(x) for x in numList])

if __name__ == '__main__':
	T = int(input().strip())
	for i in range(T):
		number = input().strip()
		sol = findLargestTidy(number)
		print('Case #{}: {}'.format(i+1, sol))