file_out = open("output.txt","w")
def findTidy(val):
	if val < 10:
		return val
	
	#print "checking for " + str(val)

	for num in range (val, 0 , -1):
		#print "looping for " + str(num)
		#arr = [int(d) for d in str(num)]
		
		if (checkSorted(num) == True):
			#print "found.."
			return num


def checkSorted(val):
	#print "checking sorted.."
	next_digit = val%10
	val = val/10
	while(val):
		digit = val %10
		if (digit > next_digit):
			#print str(val) + " not sorted"
			return False
		next_digit = digit
		val = val/10

	return True

	# if (len(arr) == 2):
	# 	prev = arr[0]
	# 	for number in range(0, 2):
	# 		if arr[number] < prev:
	# 			return False
	# 		prev = arr[number]
	# 	return True

	# if (len(set(arr)) == 1):
	# 	return True

	# if (arr[len(arr)-1] == 0):
	# 	return False

	# if( checkFirstHalf(arr, 0, len(arr)/2) == False):
	# 	return False

	# if (checkSecondHalf(arr, (len(arr)/2)+1, len(arr) - 1 ) == False):
	# 	return False


	# if (arr[len(arr)/2] > arr[len(arr) - 1]):
	# 	return False

	# if (arr[len(arr)/2] > arr[ (len(arr)/2) +1]):
	# 	return False
	
	# return True

def checkFirstHalf(arr, low, high):
	prev = arr[low]

	if (low == high):
		return True

	for number in range(low, high+1):
		if arr[number] < prev:
			return False
		prev = arr[number]
	return True

def checkSecondHalf(arr, low, high):
	prev = arr[low]

	if (low == high):
		return True

	for number in range(low, high+1):
		if arr[number] < prev:
			return False
		prev = arr[number]
	return True

f_input = open("B-small-attempt4.in.txt", "r")
tc = int(f_input.readline())

for i in range(0,tc):
	val = long(f_input.readline())
	ret = str(findTidy(val))
	file_out.write("Case #" + str(i+1) + ": " +ret + '\n')


f_input.close()
file_out.close()