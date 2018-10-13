def invite_friends(audience):
	stand_people = 0
	invited_friends = 0
	for j in range(len(audience)):
		if j > stand_people:
			invited_friends += j - stand_people
			stand_people += j - stand_people
		stand_people += audience[j]
	return invited_friends

inp = open("test.in", 'r')
t = int(inp.readline())
i = 1
res = open("res.txt", 'w')
while i <= t:
	test = inp.readline()
	max_shy, shyness = test.split()
	shyness = list(map(lambda x: int(x), list(shyness)))
	res.writelines("Case #" + str(i) + ": " + str(invite_friends(shyness)) + "\n")
	i += 1
res.close()
inp.close()