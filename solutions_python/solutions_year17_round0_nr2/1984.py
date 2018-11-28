#GCJ 2017
#B - Tidy Numbers

INFILE = "B-large.in"
OUTFILE = "B-large.out"

def tidy(a):
	string_a = str(a)
	max_order = len(string_a) - 1
	list_a = []
	for digit in string_a:
		list_a.append(int(digit))
	
	last = 0
	for i, digit in enumerate(list_a):
		if digit<last:
			b = 0
			for j, new_digit in enumerate(list_a):
				if j >= i:
					new_digit = 9
				elif j == i-1:
					new_digit = last - 1
				b += new_digit*(10**(max_order - j))
			return tidy(b)
		last = digit
	return a

fin = open(INFILE, "r")
fout = open(OUTFILE, "w")

num = fin.readline()
for case in range(int(num)):
	a = fin.readline()
	out = str(tidy(int(a)))
	fout.write("Case #" + str(case + 1) + ": ")
	fout.write(out + "\n")
	print(out)
	
fin.close()
fout.close()
