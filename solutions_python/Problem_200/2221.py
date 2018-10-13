import fileinput
import copy

num = 0;
inputs = [];

for line in fileinput.input():
	if fileinput.isfirstline():
		num = int(line)
	else:
		inputs.append(list(line.replace("\n", "")))

for idx, case in enumerate(inputs):
	# print("CASE")
	# print(case)

	casecopy = copy.deepcopy(case)
	# # print(case)
	i = 0
	# for i in range(0, len(case) - 1):
	while i < len(case):
		# print("i", str(i))
		if (i == len(case) - 1):
			break
		if int(casecopy[i]) > int(casecopy[i + 1]):
			# print("broke", str(i), str(casecopy[i]))
			casecopy[i] = str(int(casecopy[i]) - 1)

			for j in range(i + 1, len(case)):
				casecopy[j] = "9"

		# print(casecopy)
		if i == 0:
			i+=1
		elif int(casecopy[i - 1]) > int(casecopy[i]):
			i-=1
		else:
			i+=1
			# print("fix", str(casecopy))

	print("Case #" + str(idx + 1) + ": " + str(int("".join(casecopy))))
