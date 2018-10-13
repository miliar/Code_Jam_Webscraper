with open('A-small-attempt2.in') as f:
	data = f.readlines()
trials = int(data.pop(0).strip())

def makeAll():
	ans1 = []
	ans2 = []
	rows1 = []
	rows2 = []

	for i in range(trials):
		ans1.append(int(data.pop(0).strip()))
		rows1.append([])
		for j in range(4):
			rows1[i].append(data.pop(0).strip())

		ans2.append(int(data.pop(0).strip()))
		rows2.append([])
		for j in range(4):
			rows2[i].append(data.pop(0).strip())

	return ans1, ans2, rows1, rows2

def check(ans1, ans2, rows1, rows2):
		poss = []
		r1 = rows1[ans1-1].split()
		r2 = rows2[ans2-1].split()

		for num in r1:
			if num in r2:
				poss.append(num)
				if len(poss) > 1:
					return 'Bad magician!'

		if len(poss):
			return poss[0]

		return 'Volunteer cheated!'

ans1, ans2, rows1, rows2 = makeAll()
for i in range(trials):
	print 'Case #{0}: '.format(i+1) + check(ans1[i], ans2[i], rows1[i], rows2[i])
