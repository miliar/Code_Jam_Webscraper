## Calculates right space and left space for the kth person entering into a bathroom with n stalls
def stall(n, k):
	i = 0
	dict = {n:1} # Initialize size:count dictionary
	size = [n] # Initialize size list
	while i < k:
		if size[0] % 2 == 0: # if even
			left = size[0]/2 - 1
			right = left + 1
		else:
			left = size[0]/2
			right = left

		if i + dict[size[0]] >= k:
			return right, left
		else:
			i = i + dict[size[0]] # Placed dict[size[0]] people into stalls 
			
			if right not in size:
				size.append(right)
			if left not in size:
				size.append(left)
			
			if left in dict:
				dict[left] = dict[left] + dict[size[0]]
			else:
				dict[left] = dict[size[0]]
			if right in dict:
				dict[right] = dict[right] + dict[size[0]]
			else:
				dict[right] = dict[size[0]]

			del dict[size[0]]
			size = size[1:]

			
					
print stall(4,2)
print stall(5,2)
print stall(6,2)
print stall(1000,1000)
print stall(1000,1)


## I/O Handler
fIn = open('C_2.txt', 'r')
fOut = open('C_2_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
	n, k = t.split(" ")
	n = int(n)
	k = int(k)
	ans = stall(n,k)
	output = "Case #{}: {} {}\n".format(i+1,ans[0],ans[1])
	fOut.write(output)
fIn.close
fOut.close


