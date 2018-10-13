import sys
import operator

def run(n, k):
	# first person
	arr = [n]
	
	for i in range(k-1):
		#print(arr)
		# find largest entry
		# split largest entry and replace entry with two entries for split
		idx, val = max(enumerate(arr), key=lambda v: v[1])
		
		x1, x2 = split(val)
		arr[idx] = x1
		arr.insert(idx+1, x2)
		

	#print(arr)
	
	# calculate output
	# find largest entry, split, return split
	idx, val = max(enumerate(arr), key=lambda v: v[1])
	x1, x2 = split(val)
	
	return x2, x1


def split(val):
	x1 = 0
	x2 = 0
	if (val - 1) % 2 == 1:
		return int((val-2)/2), int(val/2)
	else:
		return int((val-1)/2), int((val-1)/2)


with open(sys.argv[1]) as f:
	lines = f.readlines()

with open("outC.txt", "w") as f:
	for i in range(1, len(lines)):
		arr = lines[i].split(" ")
		n = int(arr[0])
		k = int(arr[1])
		x, y = run(n, k)
		f.write("Case #{}: {} {}\n".format(i, x, y))
