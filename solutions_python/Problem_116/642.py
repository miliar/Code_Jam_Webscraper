import numpy as np
import argparse

def all_equal(row):
	let = row[1]
	if let == 'T':
		let == row[2]
	ret = True
	for e in row:
		if e == 'T' or e==let:
			ret = ret and True
		else:
			ret = ret and False

	if ret:
		if let != '.':
			return let
	return False


def check(ins):
	for _ in range(2):
		ins=ins.T
		for r in ins:
			out = all_equal(r)
			if out:
				return out

	x = range(4)
	y = range(4)
	y.reverse()

	
	out = all_equal(ins[x,x])
	if out:
		return out

	out = all_equal(ins[x,y])
	if out:
		return out

	if '.' in ins:
		return 'N'

	return 'D'



	


		







if __name__=='__main__':


	p = argparse.ArgumentParser(description='adsf')
	p.add_argument('infilename', nargs=1, help='ncs file to be converted')
	p.add_argument('outfilename', nargs=1, help='ncs file to be converted')

	args = p.parse_args()


	if args.infilename is not None and args.outfilename is not None:
		inf = open(args.infilename[0])
		outf = open(args.outfilename[0],'w')

		num = inf.readline()
		count = 0 

		for i in range(int(num)):

			ins = []
			for j in range(4):
				line = inf.readline()
				print line
				if line == '\n':
					line = inf.readline()
				ins.append([ch for ch in line if ch !='\n'])
				#inf.readline()
		
			count += 1
	
			ins = np.array(ins)	
			print ins
			outs = check(ins)
			if outs == 'X' or outs == 'O':
				ret = 'Case #%d: %s won\n'%(count,outs)
			elif outs == 'D':
				ret = 'Case #%d: Draw\n'%(count)
			else:
				ret = 'Case #%d: Game has not completed\n'%(count)
		
		
			outf.write(ret)
		
	

