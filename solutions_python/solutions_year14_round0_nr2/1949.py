in_path = r"C:\Users\Chris\Desktop\B-large.in"
out_path = r"C:\Users\Chris\Desktop\B-large-output.out"

def solve(data):
	C, F, X = (float(n) for n in data.split())
	rate, time = 2, 0

	timeTillCookies = X / rate
	timeTillFactory = C / rate
	timeAfterFactory = X / (rate + F)
	
	while timeTillCookies >= timeTillFactory + timeAfterFactory:
		time += timeTillFactory
		rate += F
		timeTillCookies = X / rate
		timeTillFactory = C / rate
		timeAfterFactory = X / (rate + F)

	return time + timeTillCookies


with open(in_path) as infile, open(out_path, "w") as outfile:
	cases = int(infile.readline())

	for i in xrange(1, cases + 1):
		data = infile.readline()
		outfile.write("Case #{0}: {1}\n".format(i, solve(data)))