num_cases = int(input())

for k in range(num_cases):
	data = input().split()
	input_str = list(data[0])
	size = int(data[1])
	
	
	result = 0
	for i in range(len(input_str) - size + 1):
		if input_str[i] == "-":
			result += 1

			for j in range(size):
				if input_str[i + j] == "-":
					input_str[i + j] = "+"

				elif input_str[i + j] == "+":
					input_str[i + j] = "-"

	if input_str.count("+") != len(input_str):
		result = "IMPOSSIBLE"
	
	
	print("Case #%d: %s" %(k + 1, result))


# if input_str[-size:].count("+") != size:
