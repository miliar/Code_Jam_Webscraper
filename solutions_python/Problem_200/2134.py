in_file = open("input.txt", "r")
out_file = open("output.txt", "w")


def solve():
	T = int(in_file.readline())
	for t in range(1, T + 1):
		out_file.write("Case #" + str(t) + ": ")
		(s,) = in_file.readline().split()
		a = []
		for x in s:
			a.append(int(x))
		found = True
		while found:
			found = False
			for i in range(len(a) - 1):
				if a[i] > a[i + 1]:
					found = True
					for j in range(i + 1, len(a)):
						a[j] = 9
					a[i] = a[i] - 1
		start = 0
		while a[start] == 0:
			start += 1
		out_file.write(''.join(str(a[i]) for i in range(start, len(a))) + "\n")


solve()

in_file.close()
out_file.close()
