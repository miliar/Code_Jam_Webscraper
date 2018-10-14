def optimized(num):
	numbers = map(int, list(num))

	pos = None
	for i in range(0,len(numbers)-1):
		if numbers[i] > numbers[i+1]:
			pos = i
			break

	if pos is None:
		return num
	else:
		while pos > 0 and numbers[pos] == numbers[pos-1]:
			pos -= 1

		return ''.join(map(str, [i for i in numbers[:pos]+[numbers[pos]-1] if i>0]))+"9"*(len(numbers)-pos-1)

if __name__ == "__main__":
	first = False
	i = -1
	with open("custom_output", 'w') as fout:
		with open("B-large.in") as f:
			for line in f:
				i += 1
				if first is False:
					first = True
				else:
					fout.write("Case #"+str(i)+": "+optimized(line.rstrip())+"\n")


