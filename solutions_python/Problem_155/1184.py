import sys

def main():
	fin = open(sys.argv[1], 'rU')
	nCases = int(fin.readline())
	case = 0
	for line in fin:
		case += 1
		smax, audience = line.strip().split(' ')
		stand = 0
		invite = 0
		for shyness in range(int(smax) + 1):
			people = int(audience[shyness])
			if stand < shyness  and people > 0:
				req = shyness - stand
				invite += req
				stand += req
			stand += people
		print('Case #{0}: {1}'.format(case, invite))


if __name__ == "__main__":
	main()