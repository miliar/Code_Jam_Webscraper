def flip_pancake(pancake, flip):
	pancake = list(pancake)
	attempt = 0
	for i in range(0, len(pancake)):
		if pancake[i] == "-":
			attempt +=1
			if (i+flip) > len(pancake):
				break
			for j in range(i, i+flip):
				if pancake[j] == "-":
					pancake[j] = "+"
				else:
					pancake[j] = "-"
	if "-" in pancake:
		return("IMPOSSIBLE")
	else:
		return(attempt)


# print(flip_pancake("-+-+-", 4))
f = open("A-small-attempt1.in")
first = True
total = 0
inputs = []

for data in f:
	if first:
		total = int(data)
		first = False
	else:
		inputs.append(data)


for i in range(0, len(inputs)):
	iteration = i+1
	pancake = inputs[i].split(' ')[0]
	flip = int(inputs[i].split(' ')[1])
	# print(pancake+flip)
	print("Case #{}: {}".format(iteration, flip_pancake(pancake, flip)))



