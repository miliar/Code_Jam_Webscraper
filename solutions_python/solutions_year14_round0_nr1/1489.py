input = open('./A-small-attempt5.in', 'r')
output = open('./out', 'w')

num_cases = int(input.readline())
for i in range(num_cases):
	output.write("Case #"+str(i+1)+": ")
	ans = []
	cards = []
	for j in range(2):
		ans.append(int(input.readline())-1)
		temp = []
		for k in range(4):
			temp.append(input.readline().split())
		cards.append(temp)
	found = 0
	for ii in range(4):
		count = cards[0][ans[0]].count(cards[1][ans[1]][ii])
		if count>0:
			found += 1
			cardFound = cards[1][ans[1]][ii]

	if found == 0:
		output.write("Volunteer cheated!")
	elif found > 1:
		output.write("Bad magician!")
	else:
		output.write(cardFound)
	found = 0
	output.write("\n")
input.close()
output.close()