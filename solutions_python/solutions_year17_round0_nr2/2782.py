array = []
num = ""
idx = 0

t = int(input())

for i in range(1, t + 1): #loops for t cases
	n = str(input())
	array = []
	num = ""

	for a in range(0,len(n)): #puts number in list
		array.append(int(n[a]))

	if len(array) == 1: #prints with array length of 1
		print("Case #{}: {}".format(i, array[0]))

	else: #if already in order
		if sorted(array) == array: 
			for y in range(0,len(array)):
				num = num+str(array[y])
			print("Case #{}: {}".format(i, num))

		else: # not in order
			while True:
				if sorted(array) == array:
					for y in range(0,len(array)):
						num = num+str(array[y])
					num = str(int(num))
					print("Case #{}: {}".format(i, num))
					break
				else:
					for b in range(0, len(array)):
						if b == 0:
							pass
						else:
							if array[b] < array[b-1]: # eg: num = 122492, array[5]<array[4]
								idx = b #gets index value
								array[b-1] = array[b-1]-1 # subtracts 1 from b-1
								break
					for c in range(0, len(array)): #substituting 9s into array
						if c >= idx:
							array[c] = 9
					continue
