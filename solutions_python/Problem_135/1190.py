def getValidNumbers(n):
	for x in range(0, 4):
		inp = input()
		if (x == (n-1)):
			inp_out = [int(x) for x  in inp.split()]
	return inp_out


def solve():
	ans_1 = int(input())
	validNumbers_1 = getValidNumbers(ans_1)
	ans_2 = int(input())
	validNumbers_2 = getValidNumbers(ans_2)

	out = set(validNumbers_1) & set(validNumbers_2)
	if (len(out) == 0):
		print("Case #"+str(x+1)+": Volunteer cheated!")
	elif (len(out) > 1):
		print("Case #"+str(x+1)+": Bad magician!")
	else:
		print("Case #"+str(x+1)+": " + str(out.pop()))


T = int(input())
for x in range(0, T):
	solve()