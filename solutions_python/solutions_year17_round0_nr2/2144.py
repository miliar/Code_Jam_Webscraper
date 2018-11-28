import sys

def main(argv):
	input_file = open(argv[1], 'r')
	output_file = open(argv[2], 'w')
	lines = [line.rstrip('\n') for line in input_file]
	for x in range(1, len(lines)):
		number = int(lines[x])
		while True:
			if check_tidy(number):
				output_file.write("Case #" + str(x) + ": " + str(number) + "\n")
				break
			else:
				number = make_tidy(str(number))
	input_file.close()
	output_file.close()

def make_tidy(number):
	n = list(number)
	for x in range(1, len(n)):
		a = len(n)-x
		if n[a] < n[a-1]:
			n[a-1] = str(int(n[a-1])-1)
			for q in range(a,len(n)):
				n[q] = "9"

	return int(''.join(n))

def check_tidy(number):
	n = str(number)
	if len(n) == 1:
		return True
	for x in range(0, len(n)-1):
		if n[x] > n[x+1] :
			return False
	return True


main(sys.argv)