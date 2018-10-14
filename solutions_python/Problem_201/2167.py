def construct(n):
	right = 0
	left = 0
	if (n % 2 == 0):
		# even
		right, left = (n//2), max(0, (n//2 - 1))
	else:
		right, left = (n//2), (n//2)
	return right, left

def get_stall(n, m):
	if (n == m):
		return 0, 0
	elif (m == 1):
		if (n % 2 == 0):
			# even
			return (n//2), max(0, (n//2 - 1))
		else:
			# odd
			return (n//2), (n // 2)
	else:
		right, left = construct(n)
		temp = [(right, left)]

		idx = 0
		while (idx != m):
			nr = temp[idx][0]
			nl = temp[idx][1]
			
			temp.append(construct(nr))
			temp.append(construct(nl))			

			idx += 1

		temp = sorted(temp, reverse=True)
		return temp[m - 1]

def main():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  n, m = [int(s) for s in input().split(" ")]

	  y, z = get_stall(n, m)
	  print("Case #{}: {} {}".format(i, y, z))
	 

if __name__ == '__main__':
	main()