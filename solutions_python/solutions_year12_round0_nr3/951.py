#!/usr/bin/python

def calc(n_str, low, up):
	ds = len(n_str)
	ret = 0
	for i in xrange(1, ds):
		s = ''
		s += n_str[i:ds]
		s += n_str[:i]

		n = int(n_str)
		m = int(s)
		if ( low <= n < m <=up and len(str(m)) == ds):
			print n,m
			ret += 1

	return ret


def main():
	file_in = open("c.in", "r")
	file_out = open("c.out", "w")

	for i in xrange(int(file_in.readline())):
		line = file_in.readline()
		nums = 0
		low = int(line.split()[0])
		up = int(line.split()[1])

		for k in xrange(low, up):
			nums += calc(str(k), low, up)

		file_out.write("Case #%s: %s\n" % (i + 1, nums))

	file_in.close()
	file_out.close()

if __name__ == "__main__":
	main()
