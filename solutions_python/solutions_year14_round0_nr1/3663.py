import sys

def check(arr1, arr2):
	n_ans = 0
	rc = 0
	for x in range(0, 4):
		for y in range(0, 4):
			if arr1[x] == arr2[y]:
				rc = arr1[x]
				n_ans += 1
	return (n_ans, rc)

def findrow(n, f):
	for i in range(0, n - 1):
		f.readline()
	nums = f.readline().rstrip().split(" ")
	nums = [int(a) for a in nums]
	# Finish the graph
	for i in range(0, 4 - n):
		f.readline()
	return nums

def solver(f, inc):
	ans1 = int(f.readline())
	arr1 = findrow(ans1, f)
	ans2 = int(f.readline())
	arr2 = findrow(ans2, f)
	checker = check(arr1, arr2)
	if checker[0] == 0:
		print "Case #" + str(inc + 1) + ": Volunteer cheated!"
	elif checker[0] > 1:
		print "Case #" + str(inc + 1) + ": Bad magician!"
	else:
		print "Case #" + str(inc + 1) + ": " + str(checker[1])
	return

def main():
	f = open(sys.argv[1])
	n_cases = int(f.readline())
	for i in range(0, n_cases):
		solver(f, i)
	return

main()