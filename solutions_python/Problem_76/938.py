import sys

def ParseTestCase(f):
	return (int(f.readline()), [int(x) for x in f.readline().split()])

def CalcForTestCase(test_case):
	return "NO" if reduce(lambda x, y: x^y, test_case) else \
		sum(test_case) - min(test_case)

if __name__ == "__main__" and len(sys.argv) == 2:
	with open(sys.argv[1]) as f:
		for i in range(int(f.readline())):
			print"Case #%d:"%(i+1), CalcForTestCase(ParseTestCase(f)[1])
	
