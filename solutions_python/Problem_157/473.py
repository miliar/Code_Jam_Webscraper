import sys
f = open(sys.argv[1])
f2 = open("res.txt", "w")

class NotFound(Exception): pass

def check(arr, expected, max_repeats, resdue=""):
	res = 1
	for index, l in enumerate(resdue):
		res = matrix[res][l]
		if res == expected:
			return resdue[index+1:], max_repeats
	fl = res
	starting = True
	while res != fl or starting and max_repeats:
		max_repeats -= 1
		starting = False
		for index, l in enumerate(arr):
			res = matrix[res][l]
			if res == expected: 
				return arr[index+1:], max_repeats
	raise NotFound("")
	

matrix = {
	-1: {"1": 1, "i":-2, "j":-3, "k":-4},
	1: {"1": 1, "i":2, "j":3, "k":4},
	-2: {"1":-2, "i":1, "j":-4, "k":3},
	2: {"1":2, "i":-1, "j":4, "k":-3},
	-3: {"1":-3, "i":4, "j":1, "k":-2},
	3: {"1":3, "i":-4, "j":-1, "k":2},
	-4: {"1":-4, "i":-3, "j":2, "k":1},
	4: {"1":4, "i":3, "j":-2, "k":-1}
}
for index in range(int(f.readline().strip())):
	L, X = map(int, f.readline().strip().split(" "))
	arr = f.readline().strip()
	try:
		resdue, X = check(arr, 2, X)
		resdue, X = check(arr, 3, X, resdue)
		counter = 0
		res = 1
		while res != 1 or counter == 0:
			counter += 1
			for l in arr:
				res = matrix[res][l]
		X = X % counter
		for l in resdue:
			res = matrix[res][l]
		for _ in range(X):
			for l in arr:
				res = matrix[res][l]
		if res != 4:
			raise NotFound("")
		f2.write("Case #{bla}: YES\n".format(bla=index+1))
	except NotFound:
		f2.write("Case #{bla}: NO\n".format(bla=index+1))

