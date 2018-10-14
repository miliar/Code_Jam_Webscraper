def main():
	f = open('C-small-attempt0.in', 'r')
	out = open('out.txt', 'w')
	T = int(f.readline())
	i = 1
	for line in f:
		A, B = line.split()
		numRecycle = findRecycle(int(A), int(B))
		out.write("Case #" + str(i) + ": " + str(numRecycle) + "\n")
		i += 1

def findRecycle(A, B):
	counts = {}
	numDigits = len(str(A))
	total = 0
	for i in range(A, B+1):
		for j in range(1, numDigits):
			k = str(i)
			kR = k[j:] + k[:j]
			kR = int(kR)
			if kR <= i or kR < A or kR > B:
				continue
			if counts.has_key(i) and kR not in counts[i]:
				counts[i].append(kR)
			else:
				counts[i] = [kR]

	for key in counts:
		total += len(counts[key])
	return total
				
	
if __name__ == "__main__":
	main()
			
