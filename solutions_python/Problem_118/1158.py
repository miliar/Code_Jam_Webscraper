import sys, math

def palindrom(number):
	number = str(number)
	rnum = number[::-1]
	rnum = str(int(rnum))
	#print number + " " + rnum
	if number == rnum:
		return True
	else:
		return False

nums = [0]
for i in range(1,1000): #10000000
	if palindrom(i) and palindrom(i*i):
		nums.append(int(nums[i-1]) + 1)
	else:
		nums.append(int(nums[i-1]))


t = raw_input("")
t = int(t)
for cases in range(1,t+1):
	sys.stdout.write("Case #" + str(cases) + ": ")
	[a,b] = raw_input("").split(' ')
	a = int(a)
	b = int(b)
	a = int(math.ceil(math.sqrt(a)))
	b = int(math.floor(math.sqrt(b)))
	#sys.stdout.write(str(a) + " " + str(b))
	sys.stdout.write(str(int(nums[b]) - int(nums[a-1])))
	sys.stdout.write("\n")
