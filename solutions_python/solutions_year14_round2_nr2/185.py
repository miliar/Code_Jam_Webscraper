def solver():
	A, B, K = [int(i) for i in input().split()]
	count = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				count += 1
	return count

def main():
	t = int(input())
	for i in range(1, t + 1):
		number = solver()
		print("Case #{:d}: {:s}".format(i, str(number)))

if __name__ == "__main__":
	main()