# nums is a list representing the ints

# iterate across list IN REVERSE
	# if L > R (left/right):
		# if R == 0:
			# new R = 9 
			# L -= 1

import sys

# Makes all numbers nines, starting with firstIdx and moving right
def trailingNines(numList, firstIdx):
	for i in range(firstIdx, len(numList)):
		numList[i] = '9'
	return numList

def main():
	filename = str(sys.argv[1])
	f = open(filename,'r')
	f.readline()
	case = 1
	for line in f:
		
		# builds list of nums as chars
		line = line.strip()
		nums = list(str(line))
		#print nums		
		# converst list items to ints
		#for i in range(len(nums)):
		#	nums[i] = int(nums[i])
		
		# iterates across list and mutates place values, right to left (decrement)
		for i in range(len(nums)-1,0,-1): # should index end at 0?
			# left and right items under cursor
			L = i-1
			R = i
			if int(nums[L]) > int(nums[R]):
				nums[L] = int(nums[L]) - 1
				nums = trailingNines(nums,R) 
		finalString = ''
		for ch in nums:
			finalString += str(ch)

		print "Case #%d: %d" % (case,int(finalString))
		case += 1
main()
					
