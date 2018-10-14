
ans = []

with open("A-large.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]

t = int(content[0])

for i in range(t):
	s, k = list(content[i+1].split(' '))
	k = int(k)

	charArr = list(s)
	no_of_flips = 0
	impossibleFlag = False

	for j in range(len(charArr)):

		if charArr[j] == '-' and j > len(s)+k:
			break

		if charArr[j] == '-' and j <= len(s)-k:
			no_of_flips += 1
			for ind in range(k):
				if charArr[j+ind] == '-':
					charArr[j+ind] = '+'
				elif charArr[j+ind] == '+':
					charArr[j+ind] = '-'

	for j in range(len(charArr)):
		if charArr[j] == '-':
			impossibleFlag = True
			break

	if impossibleFlag:
		ans.append("IMPOSSIBLE")
	else:
		ans.append(no_of_flips)

fw = open("A-large.out", "w")

for i, x in enumerate(ans):
	fw.write("Case #{0}: {1}\n".format(i+1, x))