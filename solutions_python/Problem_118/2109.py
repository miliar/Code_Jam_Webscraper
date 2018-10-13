import sys
import math

def is_palindrome(integer):
	i = list(str(integer))
	l = len(i)
	if l == 1:
		return True
	mid = l / 2
	for idx in xrange(0, mid):
		if i[idx] != i[l - idx - 1]:
			return False
	return True


def main(argv):
	f = open(argv[0])
	out = open('out.txt', 'w')

	T = int(f.readline())
	for case in xrange(0, T):
		start, end = f.readline().strip().split(' ')
		start = int(math.ceil(math.sqrt(int(start))))
		end   = int(math.floor(math.sqrt(int(end))))
		count = 0
		for x in xrange(start, end + 1):
			if is_palindrome(x) and is_palindrome(x ** 2):
				count += 1
		out.write("Case #%d: %d\n" % (case + 1, count))

	f.close()
	out.close()

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))