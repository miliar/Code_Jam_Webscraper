#!/usr/bin/python3
t = input()
t = int(t)
for test in range(t):
	cards = []
	for i in range(2):
		row = int(input())
		for r in range(4):
			numbers = input()
			if (row == r+1):
				cards.append([int(x) for x in numbers.split(" ")])
	cnt = 0
	res = 0
	for num in cards[0]:
		if (num in cards[1]):
			res = num
			cnt += 1
	if (cnt == 0):
		print ("Case #" + str(test+1) + ": Volunteer cheated!")
	elif (cnt == 1):
		print ("Case #" + str(test+1) + ": " + str(res))
	else:
		print ("Case #" + str(test+1) + ": Bad magician!")
