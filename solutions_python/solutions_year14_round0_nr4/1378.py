import sys
sys.setrecursionlimit(100000)

# functions
def y(n, k):
	# sac my smallest to take his largest
	score = 0
	while len(n) > 0:
		if n[0] < k[0]:
			# if mine is the smallest, sac it to take his largest
			del n[0]
			del k[-1]
		else:
			# i pick up a win with my smallest
			del n[0]
			del k[0]
			score += 1
	return score

def z(n, k):
	# play low to high
	while len(n) > 0:
		i = 0
		while i < len(k) and k[i] < n[0]:
			i += 1
		if i == len(k):
			return i
		else:
			# k plays k[i] piece and we play n[0]
			del n[0]
			del k[i]
	return 0
	

	

# get the file
f = open(sys.argv[1])

count = int(f.readline().strip())

# to list
for i in range(count):
	j = int(f.readline().strip())
	n = sorted([float(x) for x in f.readline().strip().split()])
	k = sorted([float(x) for x in f.readline().strip().split()])
	print("Case #" + str(i+1) + ": " + str(y(list(n),list(k))) + " " + str(z(list(n),list(k))))

