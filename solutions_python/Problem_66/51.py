import math

def recursive(array):
	if (0 >= reduce(max, array)):
		return 0
	if (len(array) == 2):
		return 1
	array = map(lambda x: x-1, array)
	return 1 + recursive(array[:len(array)/2]) + recursive(array[len(array)/2:])
		

def getResult(p,array,costs):
	array = map(lambda x: p-x, array)
	return recursive(array)

	
if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		p = int(f.readline().strip())
		array = map(int,f.readline().strip().split(" "))
		costs = range(0,p)
		for j in range(0,p):
			costs[j] = map(int,f.readline().strip().split(" "))
		ans = 0
		ans = getResult(p,array,costs)
		print "Case #%d: %s" %(i,ans)