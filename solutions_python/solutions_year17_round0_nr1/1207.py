# Vendula Poncova

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

T = int(input())
for i in range(1, T + 1):

	line = input().split(" ")
	S = line[0]
	K = int(line[1])
	current_flips = 0
	total_flips = 0


	flips = [0] * (len(S) + 1)
	#print(S, K)

	
	for j, s in enumerate(S):
		current_flips += flips[j]

		if s == "+":
			if current_flips % 2 == 1:
				if j + K < len(S) + 1:
					total_flips += 1
					current_flips += 1
					flips[j + K] -= 1
				else:
					total_flips = "IMPOSSIBLE"
					break

		elif s == "-":
			if current_flips % 2 == 0:
				if j + K < len(S) + 1:
					total_flips += 1
					current_flips += 1
					flips[j + K] -= 1
				else:
					total_flips = "IMPOSSIBLE"
					break

		#print(total_flips, current_flips, s, j, j + K, flips)

	print("Case #{}: {}".format(i, total_flips))
