def seg(nSeg, segSize):
	if(segSize %2 == 0):
		return [(nSeg, segSize/2), (nSeg, (segSize/2)-1)]
	else:
		return [(2*nSeg, (segSize-1)/2)]

def find(n, k):
	nPlaced = 0
	lmin, lmax = 0, 0
	segments = {n:1}
	while nPlaced < k:
		maxSegment = max(list(segments.keys()))
		segSize, nSeg = maxSegment, segments.pop(maxSegment)
		newS = seg(nSeg, segSize)
		for s in newS:
			if(s[1] in segments):
				segments[s[1]] += s[0]
			else:
				segments[s[1]] = s[0]

		nPlaced += nSeg

		lmax = (segSize - 1) / 2 if segSize % 2 != 0 else segSize / 2
		lmin = (segSize - 1) / 2 if segSize % 2 != 0 else (segSize / 2) - 1

	return(lmax, lmin)

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
					n, k = l.split(' ')
					lmax, lmin = find(int(n), int(k))
					fout.write('Case #{}: {} {}\n'.format(i, int(lmax), int(lmin)))
