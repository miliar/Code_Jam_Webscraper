T = int(input().strip())

def naive(s):
	for i in range(s, 0, -1):
		k = str(i)
		good = True
		for j in range(len(k)-1):
			if k[j] > k[j+1]:
				good = False
				break
		if good:
			return k
	
	return ""

def test(s):
	for i in range(len(s)-1):
		if s[i] < s[i+1]:
			return False
	return True

def fixit(s):
	k = [x for x in str(s)[::-1]]
	b = [False for x in str(s)]
	while not test("".join(k)):
		for i in range(len(k)-1):
			if k[i] < k[i+1]:
				k[i] = "9"
				if not b[i+1]:
					k[i+1] = str(int(k[i+1])-1)
				b[i] = True
	if k[-1] <= "0":
		return "".join(k[:-1][::-1])
	return "".join(k[::-1])



for i in range(T):
	s = int(input().strip())
	#s = str(i)

	if len(str(s)) == 1:
		print("Case #" + str(i+1) + ": " + str(s))
		continue

	print("Case #" + str(i+1) + ": " + fixit(s))