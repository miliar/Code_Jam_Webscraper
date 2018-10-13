T = int(raw_input())
for i in range(0, T):
	first = int(raw_input())
	data = []
	for j in range(0, 4):
		data.append([map(int, raw_input().split())])
	FirstRow = data[first-1][0]
	data = []
	second = int(raw_input())
	for k in range(0, 4):
		data.append([map(int, raw_input().split())])
	SecondRow = data[second-1][0]
	intersection = [x for x in FirstRow if x in SecondRow]
	message = ""
	if len(intersection) > 1:
		message = "Bad magician!"
	elif len(intersection) == 1:
		message = str(intersection[0])
	else:
		message = "Volunteer cheated!"
	print("Case #{0}: {1}".format(i+1, message))



