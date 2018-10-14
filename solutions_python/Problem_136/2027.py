def findTime(C, F, X):
	rate = 2
	seconds = 0	
	best_so_far = X/rate
	if rate == X:
		return "{:.7f}".format(1)
	while (1):
		farm = C/rate
		seconds += farm
		rate += F
		rem = X/rate
		poss = seconds + rem
		if poss > best_so_far:
			break
		best_so_far = poss
	return "{:.7f}".format(best_so_far)

def main():
	num_tests = int(input())
	for i in range(1, num_tests + 1):
		inp = input().split(" ")
		inp = [float(x) for x in inp]
		C = inp[0]
		F = inp[1]
		X = inp[2]

		print("Case #" + str(i) + ":" + " ", end="")
		print(findTime(C, F, X))

if __name__ == "__main__":
	main()