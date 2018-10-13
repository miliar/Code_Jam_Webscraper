def start(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	numTest = int(lines[0])
	tidyMain(numTest, lines[1:])


def tidyMain(numTest, inputs):
	output = open('tidy_large_output.in', 'w')
	for i in xrange(numTest):

		res = tidy(i, inputs[i])
		output.write(res + '\n')
	output.close()

def tidy(k, num):
	num = list(str(num))
	num= [int(elem) for elem in num]

	while not check(num):
		for i in xrange(len(num)):
			if i != 0 and num[i] < num[i - 1]:
				num[i - 1] -= 1
				for j in range(i, len(num[i:]) + i):
					num[j] = 9
				break
	num= [str(elem) for elem in num]
	return "Case #" + str(k + 1) + ": " + str(int(''.join(num)))


def check(num):
	for i in xrange(len(num)):
		if i != 0 and num[i] < num[i - 1]:
			return False
	return True

start('B-large.in')