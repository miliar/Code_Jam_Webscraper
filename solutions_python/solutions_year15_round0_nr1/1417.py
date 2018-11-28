from sys import stdin

def handle_case(shynesses):
	# All standing	
	if len(shynesses) == 1:
		return 0

	standing = shynesses[0]
	additional = 0
	for i in xrange(1, len(shynesses)):
		if standing < i:
			additional += (i - standing)
			standing += (i - standing)
		standing += shynesses[i]

	return additional


def main():
	for i in xrange(int(stdin.readline())):
		_, shynesses = stdin.readline().strip().split(" ")
		print "Case #{}: {}".format(i + 1, handle_case([int(x) for x in shynesses]))


if __name__ == "__main__":
	main()