__author__ = 'genes'

from itertools import islice

case = 0
def format_print(message):
	global case
	case += 1
	print "Case #%s: %s" % (case, message)

def check(guesses):
	a, b = int(guesses[0]), int(guesses[5])
	# Cards intersection
	result = reduce(lambda x, y: x & y, map(lambda x: set(x.strip().split(" ")),
											(guesses[a], guesses[b + 5])))
	if len(result) == 1:
		format_print(result.pop())
	elif len(result) > 1:
		format_print("Bad magician!")
	else:
		format_print("Volunteer cheated!")

def main():
	with open('A-small-attempt0.in', 'r') as fd:
		for _ in xrange(int(fd.readline())):
			test_case = list(islice(fd, 10))
			check(test_case)

if __name__ == '__main__':
	main()