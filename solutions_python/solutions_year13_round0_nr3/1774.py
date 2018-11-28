import math
inputfile = open("input.txt", "r")
outputfile = open("output.txt", "w")

n = 0

def pal(num):
	num = str(num)
	y = ''.join(reversed(num))
	return y == num


def func():
	global n
	temp = inputfile.readline()
	n = int(temp)
	nums = [0 for i in range(n)]
	L = []
	for i in range(n):
		a = inputfile.readline()
		a = a.split()
		a[0], a[1] = int(a[0]), int(a[1])
		L.append(a)
	print n,L

	for i in range(n):
		limits = L[i]
		for j in range(limits[0], limits[1] + 1):
			
			if pal(j) == True:
				
				square = math.sqrt(j)
				
				if square % 1 == 0:
					
					if pal(int(square)):
						
						nums[i] += 1
					
		
	print nums
	for i in range(n):
		print "Case #" + str(i + 1) + ": " + str(nums[i])
		outputfile.write("Case #" + str(i + 1) + ": " + str(nums[i]) + '\n')




func()