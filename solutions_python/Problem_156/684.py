

if __name__== "__main__":
	f = open("B-large.in")             
	line = f.readline()             
	for t in range(int(line)):
		XXX = int(f.readline())
		YYY = f.readline().split()
		arr = list(map(int, YYY))
		ans = max(arr)
		Z = 2
		while Z < ans:
			ans = min(ans, sum([(x - 1) // Z for x in arr]) + Z)
			Z += 1
		print('Case #%d: %s' % (t + 1, ans))
	f.close()
