def main():
	for TEST in range(1, int(input())+1):
		D, N = map(int, input().split())

		ksPairs = [list(map(int, input().split())) for i in range(N)]

		maxTime = 0
		for K, S in ksPairs:
			time = (D - K) / S
			if maxTime < time:
				maxTime = time

		speed = D / maxTime

		print("Case #{}: {}".format(TEST, speed))

main()
