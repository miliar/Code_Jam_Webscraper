#diccionarios {}
#listas [] 
import sys
args = sys.argv
filename = open(sys.argv[1])
out = open("a.out",'w+')

def rings(r, t):
	count = 0
	n = 1
	while t > 0:
		t = t - ((r+n)**2 - (r+n-1)**2)
		if t >= 0:
			count += 1
		n += 2
	return count





filename.readline();#first line
i = 1
while 1:
	line = filename.readline()
	if not line:
		break
	nums = line.split()
	#print("Case #" + str(i) + ": " + str(rings(int(nums[0]),int(nums[1]))))
	out.write("Case #" + str(i) + ": " + str(rings(int(nums[0]),int(nums[1]))) + "\n")
	i += 1
	
