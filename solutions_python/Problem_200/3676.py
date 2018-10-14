import sys

def run(x):
	arr = list(map(int, list(x)))
	
	l = len(arr)
	i = l-1
	while i > 0:
		if arr[i] < arr[i-1]:
			arr[i] = 9
			arr[i-1] = arr[i-1] - 1
			for j in range(i, l):
				arr[j] = 9
		
		i = i - 1
	
	return str(int("".join(map(str, arr))))


with open(sys.argv[1]) as f:
	lines = f.readlines()

with open("outA.txt", "w") as f:
	for i in range(1, len(lines)):
		res = run(lines[i][:-1])
		f.write("Case #{}: {}\n".format(i, res))
		print("Case #{}: {}".format(i, res))



