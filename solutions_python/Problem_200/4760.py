import sys

def tidy(nums):
    out = []
    while(True):
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                out.append(nums[i])
            else:
                out.append(nums[i]-1)
                for j in range(i,len(nums)-1):
                    out.append(9)
                break
        if check(out) == 1:
            return out

			
def check(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return -1
    return 1     


input = [row.rstrip('\n') for row in open(sys.argv[1])]
input = input[1:]
output = open ( sys.argv[2] , 'w' )

counter = 1
for num in input: 
	nums = [int(i) for i in str(num)]
	if len(nums) == 1: 
		sout  = ""
		for j in nums:
			sout  = sout + str(j)
		if sout [0] == "0":
			sout = sout [1:] 
		output.write("Case #" + str(counter) + ": " + sout + "\n" )
	else: 
		if check(nums) == 1 :
			sout = ""
			for j in nums:
				sout = sout + str(j)
			if sout [0] == "0":
				sout = sout [1:]
			output.write("Case #" + str(counter) + ": " + sout + "\n" )
		else: 
			temp = tidy(nums)
			sout = ""
			for i in temp:
				sout = sout + str(i)
			if sout [0] == "0":
				sout = sout [1:] 
			output.write("Case #" + str(counter) + ": " + sout  + "\n" )
	counter += 1
output.close()
