def candysplit(nums):
	for i in range(17):
		x = 0
		for num in nums:
			x ^= (num & 1<<i)
		if x:
			#print x
			return False
	return sum(nums) - min(nums)

def handleLine(line):
	return candysplit(map(lambda x:int(x),line.split(' '))) or "NO"
	
def solveCandy():
	f = open('gcjdata.txt','r')
	lines = f.readlines()
	for i in range(2,len(lines),2):
		print "Case #{0}: {1}".format(i/2,handleLine(lines[i]))
		
solveCandy()