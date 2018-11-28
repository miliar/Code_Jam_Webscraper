import sys

def main():
	name, pathin, pathout = sys.argv

	filein = open(pathin)
	fileout = open(pathout,'w')

	total = int(filein.readline())
	results = []
	for case in range(total):
		seq = filein.readline().split()[0]
		results.append(solve(seq))


	for i, result in enumerate(results):
		fileout.write('Case #%s: %s\n'%(i+1, result))



def solve(seq):
	if not seq:
		return ''

	peak = max(list(seq))

	pos = 0
	for i in range(len(seq)):
		if seq[i] == peak:
			pos = i

	# print(seq[pos], seq[:pos], seq[pos+1:])
	return seq[pos]+solve(seq[:pos])+seq[pos+1:] 

if __name__ == '__main__':
	main()

