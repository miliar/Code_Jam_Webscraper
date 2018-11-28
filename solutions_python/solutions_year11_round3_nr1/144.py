def solve(R, C, data):
	for i in range(R):
		for j in range(C):
			if data[i][j] == '#':
				if i < R - 1 and j < C - 1 and data[i+1][j] == data[i][j+1] == data[i+1][j+1] == '#':
					data[i][j] = '/'
					data[i+1][j] = '\\'
					data[i][j+1] = '\\'
					data[i+1][j+1] = '/'
				else:
					return "Impossible"
	output = ""
	for i in range(R):
		output += "".join(data[i]) + "\n"
	return output[:-1]

def main():
	T = input()
	for i in range(T):
		R, C = [int(j) for j in raw_input().split()]
		data = []
		for j in range(R):
			data.append(list(raw_input().strip()))
		print "Case #%d:\n%s" % (i+1, solve(R, C, data))
main()

