def tidy(n):
	for i in range(len(n)-1, 0, -1):
		if n[i] < n[i-1]:
			return False
	return True

def less_tidy(n):

	if tidy(n):
		return n

	for i in range(len(n)-1, 0, -1):
		if (n[i] < n[i-1]):
			if (n[i] == "0"):
				n = list(str(int(''.join(n))-10**(len(n)-1-i)))
			else:
				n[i-1] = str(int(n[i-1])-1)

			for j in range(len(n)-1, i-1, -1):
				n[j] = "9"

	return less_tidy(n)

count = 0
file = open("ex2.txt", "r")
for line in file:
	if count == 0:
		count = count + 1
		continue
	n = less_tidy(list(str(line.replace("\n", "").replace(" ",""))))
	print("Case #{}: {}".format(count, int(''.join(n))))
	count = count + 1