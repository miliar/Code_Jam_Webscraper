def flip_pancakes(s, k):
	s = list(s)
	counter = 0
	for i in range(len(s)):
		if(s[i] == '+'):
			continue
		elif(i > len(s)-k):
			return -1
		else:
			for j in range(i, i+k):
				s[j] = '+' if s[j] == '-' else '-'
			counter += 1
	return counter

FILE_NAME = "C:\\users\\avivr\\desktop\\A-large.in"
OUT_FILE_NAME = "C:\\users\\avivr\\desktop\\out.txt"

f = open(FILE_NAME)
fo = open(OUT_FILE_NAME, 'w')
n = int(f.readline())

for i in range(n):
	line = f.readline().strip().split()
	s = line[0]
	k = int(line[1])
	res = flip_pancakes(s, k)
	if res == -1:
		res = "IMPOSSIBLE"
	else:
		res = str(res)
	fo.write("case #" + str(i + 1) + ": " + res + "\n")
f.close()
fo.close()