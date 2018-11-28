from sys import stdin

def numRecycled(A, B):
	count = 0
	if len(A) == len(B) and int(A) < int(B) and len(A) > 1:
		for i in range(int(A), int(B)):
			i_string = str(i)
			recycledValues = []
			for j in range(len(i_string)):
				recycledValues.append(i_string)
				i_string = i_string[-1] + i_string[:-1]
			recycledValues = set(recycledValues)
			for j in range(i+1, int(B)+1):
				if str(j) in recycledValues:
#					print i, ':', j
					count += 1
	return count

def main():
	cases = int(stdin.readline())
	lines = stdin.readlines()
	for line in range(len(lines)):
		pair = lines[line].split()
		A = pair[0]
		B = pair[1]
		print 'Case #{}: {}'.format(line+1, numRecycled(A, B))

if __name__ == '__main__':
  main()
