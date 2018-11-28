t = int(raw_input())

for i in range(1, t + 1):
	numbers = [int(n) for n in raw_input()]
	count = len(numbers)

	#print(count)
	if (count == 1):
		print "Case #{}: {}".format(i, numbers[0])
		continue
	while True:
		converted = True
		for j in range(count-1):
			#print(numbers[j], numbers[j+1], numbers)
			if (numbers[j] > numbers[j+1]):
				numbers[j] = numbers[j] - 1
				if (numbers[j] == 0 and j == 0):
					for k in range(j+1, count):
						numbers[k] = 9
					break
				else:
					for k in range(j+1, count):
						numbers[k] = 9
					converted = False
		#print(numbers, converted)
		if (converted == True):
			break

	print "Case #{}: {}".format(i, int(''.join(map(str, numbers))))

	#