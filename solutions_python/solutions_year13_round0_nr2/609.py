import numpy as np
import argparse



def row_elim(lawn):

	needs = list()

	for row in lawn:
		need = []
		if max(row)==min(row):
			need = [0]*len(row)
		else:
			m = max(row)
			for col in row:
				if col < m:
					need.append(col)
				else:
					need.append(0)
		needs.append(need)


	return np.array(needs)

def col_check(lawn,roE):
	lawnT = lawn.T
	rowET = rowE.T

	for i in range(len(lawnT)):
		row = lawnT[i,:]
		need = rowET[i,:]
		h = max(need)
		if h == 0:
			continue
		for (r,n) in zip(row,need):
			if (n != h and n!=0) or (n==0 and r>h):
				return False

	return True




if __name__ == '__main__':


	p = argparse.ArgumentParser(description='adsf')
	p.add_argument('infilename', nargs=1, help='ncs file to be converted')
	p.add_argument('outfilename', nargs=1, help='ncs file to be converted')

	args = p.parse_args()


	inf = open(args.infilename[0])
	outf = open(args.outfilename[0],'w')

	num = inf.readline()

	for i in range(int(num)):

		(yN,xN) = [int(e) for e in inf.readline().split()]

		lawn = []
		for y in range(yN):
			row = [int(e) for e in inf.readline().split()]
			lawn.append(row)
		lawn = np.array(lawn)
	
		rowE = row_elim(lawn)

		outs = col_check(lawn,rowE)
		if outs:
			outf.write('Case #%d: YES\n'%(i+1))
		else:
			outf.write('Case #%d: NO\n'%(i+1))

