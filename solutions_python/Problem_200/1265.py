with open("B-large.in") as f:
	with open("output.txt", "w") as g:
		t = int(f.readline().strip())
		for i in range(1, t + 1):
			n = f.readline().strip()
			for j in range(len(n) - 2, -1, -1):
				if int(n[j]) > int(n[j + 1]):
					n = n[:j] + str(int(n[j]) - 1) + "9" * (len(n[j + 2:]) + 1)
			n = n.lstrip("0")
			g.write("Case #{}: {}\n".format(i, n))
