def solve(smax, s):
	res = 0
	standing = 0
	for i, x in enumerate(s):
		if standing < i:
			res += i-standing
			standing = i
		standing += x
	return res

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		smax, seq = raw_input().split(' ')
		print "Case #{0}: {1}".format(i, solve(smax, map(int, list(seq))))

if __name__ == '__main__':
	main()