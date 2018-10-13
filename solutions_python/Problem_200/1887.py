def lastTidyNumber(n):
	sn = str(n)
	isTidy = True
	tidyIndex = 0
	for c in range(0, len(sn)-1):
		if int(sn[c+1]) < int(sn[c]):
			tidyIndex = c
			isTidy = False

	if isTidy:
		return int(n)
	else:
		nn = sn[:tidyIndex] + str(int(sn[tidyIndex])-1) + '9'*len(sn[tidyIndex+1:])
		return lastTidyNumber(nn)

import sys
if __name__ == '__main__':
	inputPath = sys.argv[1]
	outputPath = sys.argv[2]
	with open(inputPath, 'r') as f:
		with open(outputPath, 'w') as fout:
			text = f.read().splitlines()
			for i, l in enumerate(text):
				if (i == 0):
					continue
				else:
					n = int(l)
					tidy = lastTidyNumber(n)
					fout.write('Case #{}: {}\n'.format(i, tidy))
