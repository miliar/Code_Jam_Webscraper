import sys

def return_gcd(a, b):
	if b == 0:
		return a
	else:
		return return_gcd(b, (a % b))


input_stream = sys.stdin
output_stream = sys.stdout

t = int(input_stream.readline().strip())

for i in range(t):
	values = input_stream.readline().split()
	n = int(values[0])
	pd = int(values[1])
	pg = int(values[2])

	possible = False

	gcd = return_gcd(pd, 100)
	min_games = int(100 / gcd)

	if ((min_games <= n) and not(((pg == 0) and (pd > 0)) or ((pg == 100) and (pd < 100)))):
		possible = True

	output_stream.write("Case #" + str(i + 1) + ": ")
	if possible:
		output_stream.write("Possible\n")
	else:
		output_stream.write("Broken\n")


input_stream.close()
output_stream.close()
