import sys

inputpath = sys.argv[1]
outpath = sys.argv[2]


with open(inputpath, "r") as f:
	out = open(outpath, "w")
	T = int(f.readline())
	for case in range(T):
		R, C, W = map(int, f.readline().split())

		result = int(R*(C/W)+W-1)
		if C % W != 0:
			result += 1

		out.write("Case #{}: {}\n".format(case+1, result))
		print("Case #{}: {}".format(case+1, result))
	out.close()
