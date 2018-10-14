# t = int(input())
# for i in range(1, t + 1):
# 	line = input()
# 	k = int(input())
# 	print("Line:{}, K:{}".format(line, k))
# 	# n,m = [int(s) for s in input().split(" ")]
# 	# print("Case #{}: {} {}".format(i, n + m, n * m))

# input T
t = int(input())
for i in range(0, t):
	max = 0
	#input N
	n = int(input())
	for l in range(1, n + 1):
		#take next number
		# print("____________")
		numberString = str(l)
		length = len(numberString)
		array = []

		for k in range(0, length):
			array.append(int(numberString[k]))
		# print(array)
		# print(array[0])

		isGood = True
		for a in range(0, len(array)):
			znak = array[a]
			if a > 0:
				if array[a] < array[a-1]:
					isGood = False
					# print("f")
		if isGood:
			max = l		
	print("Case #{}: {}".format(i+1,max))
