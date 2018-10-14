import math
pals = []
for i in range(1001):
	c = True
	for a in range(len(str(i))):
		if str(i)[a] != str(i)[-1 * a - 1]:
			c = False
			break
	if c:
		d = True
		for b in range(len(str(int(math.sqrt(i))))):
			if str(int(math.sqrt(i)))[b] != str(int(math.sqrt(i)))[-1 * b - 1] or int(math.sqrt(i)) ** 2 != i:
				d = False
				break
		if d:
			pals.append(i)
myin = open("fair.in", "r")
myout = open("fair.out", "w")
t = int(myin.readline()[:-1])
data = []
for i in range(t):
	a = myin.readline()[:-1]
	for b in range(len(a)):
		if a[b] == " ":
			data.append([int(a[:b]), int(a[b+1:])])
result = []
for i in data:
	result.append([])
	for a in pals:
		if i[0] <= a and a <= i[1]:
			result[-1].append(a)
for i in range(len(result)):
	myout.write("Case #" + str(i + 1) + ": " + str(len(result[i])) + "\n")
