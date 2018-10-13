def checkTidyNaive(n):

	tidy = True

	if n > 9:
		s = str(n)
		for i in range(1, len(s), 1):
			if int(s[i-1]) > int(s[i]):
				tidy = False
				break

	return tidy

def processNaive(n):

	lastTidy = n
	if not checkTidyNaive(lastTidy):
		while not checkTidyNaive(lastTidy):
			lastTidy -= 1
			print(lastTidy)

	return lastTidy

def processSmart(n):

	lastTidy = n

	if not checkTidyNaive(lastTidy):

		s = str(lastTidy)
		a = 0
		b = 1
		while(b != len(s)):
			if s[a] == s[b]:
				b += 1
			elif s[a] < s[b]:
				a = b
				b += 1
			elif s[a] > s[b]:
				break

		if b < len(s):
			innocent = s[:a]
			culprit = s[a:]
			x = str(int(culprit[0]) - 1)
			y = str(pow(10, len(culprit) - 1) - 1)
			z = x + y

			if innocent != "":
				lastTidy = int(innocent + z)
			else:
				lastTidy = int(z)

	return lastTidy

def main():

	if True:
		t = int(input())
		for i in range(1, t + 1):
		  n = int(input())
		  lastTidy = processSmart(n)
		  print("Case #" + str(i) + ": " + str(lastTidy))
	else:
		n = 100
		lastTidy = processSmart(n)
		print("Case #" + str(1) + ": " + str(lastTidy))

if __name__ == "__main__":
	main()