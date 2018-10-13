def tidy_nums(N):
	digits = list(str(N))
	last = len(digits)
	for i in range(len(N) - 2, -1, -1):
		if(digits[i] <= digits[i + 1]):
			continue
		else:
			digits[i] = str(int(digits[i]) - 1)
			for j in range(i+1, last):
				digits[j] = '9'
			last = i + 1
	return int("".join(digits))



FILE_NAME = "C:\\users\\avivr\\desktop\\B-large.in"
OUT_FILE_NAME = "C:\\users\\avivr\\desktop\\out.txt"

f = open(FILE_NAME)
fo = open(OUT_FILE_NAME, 'w')
n = int(f.readline())

for i in range(n):
	line = f.readline().strip().split()
	N = line[0]
	res = str(tidy_nums(N))
	fo.write("case #" + str(i + 1) + ": " + res + "\n")
f.close()
fo.close()