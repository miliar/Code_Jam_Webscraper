file = open("A-large.in", "r")
newFile = open("output.txt", "w")

def Flipped(s:str, k:int):
	for i in range (len(s)):
		if (s[i] == "-"):
			start, end = i, (i + k)
			if (k > (len(s) - i)):
				start = len(s) - k
				end = len(s)

			n = s[start:end]
			x = ""
			for j in range(k):
				x += "+" if (n[j] == "-") else "-"
			return s[:start] + x + s[end:]
	return s

def CountPancakeFlips(s:str, k:int):
	if ("-" not in s):
		return 0
	count = 0
	x = s
	while True:
		n = x
		x = Flipped(x, k)
		count += 1
		if ("-" not in x):
			return count
		elif (n == Flipped(x, k)):
			return -1
	return 0


testCases = int(file.readline())
for i in range(testCases):
	x = file.readline().split(" ")
	count = CountPancakeFlips(x[0], int(x[1]))
	s = "Case #{}: {}".format(i + 1, (count if (count >= 0) else "IMPOSSIBLE"))
	if (not i == testCases - 1):
		s += "\n"
	newFile.write(s)

file.close()
newFile.close()
