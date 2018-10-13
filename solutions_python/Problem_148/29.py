T = int(raw_input())
for tt in range(T):
	ii = raw_input().split(" ")
	numOfFile = int(ii[0])
	diskSize = int(ii[1])
	files = map(int, raw_input().split(" "))
	files = sorted(files)
	files = files[::-1]
	used = [0]*len(files)
	result = 0
	for fi in range(len(files)):
		if used[fi] == 0:
			used[fi] = 1
			for fii in range(fi+1, len(files)):
				if used[fii] == 0 and files[fii]+files[fi]<=diskSize:
					used[fii] = 1
					break
			result += 1
	print "Case #{0}: {1}".format(str(tt+1), str(result))