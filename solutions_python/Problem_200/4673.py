def tidy(max):
	for num in range(max, 0, -1):
		tidy = False
		previous = -999;
		for num_str in str(num):
			if int(num_str) >= previous:
				tidy = True
			else:
				tidy = False
				break
			previous = int(num_str)

		if(tidy):
			return num


# print(tidy(7))

# total = input()
result = []
inputs = []
total = 999
f = open("B-small-attempt1.in", "r")
first = True
for num in f:
	if first:
		total = int(num)
		first = False
	else:
		inputs.append(int(num))

for i in range(0, len(inputs)):
	iteration = i+1
	num = int(inputs[i])
	# print(inputs[i])
	print("Case #{}: {}".format(iteration, tidy(num)))

# tidy = False
# previous = -999;
# for num_str in str(4):
# 	if int(num_str) >= previous:
# 		tidy = True
# 	else:
# 		tidy = False
# 		break
# 	previous = int(num_str)
# print(tidy)
