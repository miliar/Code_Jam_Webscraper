def find_tidy(num):
	for i in range(int(num), 0, -1):
		if int("".join(sorted(list(str(i))))) == i:
			return i

t = int(input())
for i in range(1, t + 1):
	num = input()
	print ("Case #{}: {}".format(i, find_tidy(num)))