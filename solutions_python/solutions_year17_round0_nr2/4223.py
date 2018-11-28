import sys

def tidyNumber(inp):
	i = 0
	j = 1
	out = []
	inp = str(inp)
	if len(inp) == 1:
		return inp
	while i < len(inp)-1:
		if int(inp[i]) <= int(inp[j]):
			out.append(inp[i])
			if i == len(inp)-2:
				out.append(inp[j])
			i = i+1
			j = j+1
		else:
			out.append(str(int(inp[i]) -1))
			if i == 0:
				break
			while (int(out[i]) == 0) or (out[i-1]>out[i]):
				if i == 0:
					break
				out[i] = str(9)
				out[i-1] = str(int(out[i-1]) -1)
				i = i-1
			break
	return (''.join(out)+ str(9)*(len(inp)-len(out))).strip('0')


def read():
        output = [line.strip() for line in open(sys.argv[1], "r")]
        final = open(sys.argv[2], "w")
        test_cases = output[0]
        for i in range(int(test_cases)):
                final.write("Case #"+str(i+1)+": "+tidyNumber(output[i+1])+"\n")
        final.close()

if __name__ == "__main__":
        read()
