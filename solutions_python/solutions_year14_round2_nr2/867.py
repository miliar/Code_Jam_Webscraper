import itertools

in_path = r"C:\Users\Chris\Desktop\B-small-attempt0.in"
out_path = r"C:\Users\Chris\Desktop\B-small.out"



def solve(data):
	A, B, K = (int(i) for i in data.split())

	return len(list((a, b) for (a, b) in itertools.product(range(A), range(B)) if a & b < K))
	

with open(in_path) as infile, open(out_path, "w") as outfile:
	cases = int(infile.readline())
	

	for i in range(1, cases + 1):
		data = infile.readline()

		outfile.write("Case #{0}: {1}\n".format(i, solve(data)))