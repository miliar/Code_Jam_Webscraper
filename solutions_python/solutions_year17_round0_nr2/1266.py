# Vendula Poncova

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

T = int(input())
for i in range(1, T + 1):

	N = [int(n) for n in input()]
	prev = 0
	pointer = -1
	same = 1
	
	print("Case #{}: ".format(i), end="")
	
	for j, n in enumerate(N):
		if prev < n:
			same = 1
		elif prev == n:
			same += 1
		else:
			pointer = j
			break

		prev = n

	if pointer == -1:
		for m in N:
			print(m, end="")
	else:
		skip_zero = True

		for m in N[:j-same]:
			if not (skip_zero and m == 0):
				skip_zero = False				
				print(m, end="")

		if not (skip_zero and N[j-same] - 1 == 0):
			skip_zero = False
			print(N[j-same] - 1, end="")

		for m in N[j-same+1:]:
			print(9, end="")

	print("")

