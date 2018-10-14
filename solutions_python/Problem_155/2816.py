


if __name__ == "__main__":
	T = input()
	for i in range(T):
		smax, s = raw_input().split(" ")
		standing = 0
		friends = 0
		for j in range(int(smax)+1):
			if standing < j:
				friends += 1
				standing += 1
			standing += int(s[j])
			# print "F:%d, S:%d" % (friends, standing)

		print "Case #%d: %d" % (i+1, friends)