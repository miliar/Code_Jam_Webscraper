import argparse
import numpy as np

def comp(r,t):
	#print long(max(np.roots([2,3+2*r,-t])))
	i = 0
	s = float(0)
	while s <= t:
		s += (r+1+2*i)**2
		s -= (r+2*i)**2
		i += 1
	return i-1
	
	


if __name__=='__main__':
	
	
	p = argparse.ArgumentParser(description='adsf')
	p.add_argument('infilename', nargs=1, help='ncs file to be converted')
	p.add_argument('outfilename', nargs=1, help='ncs file to be converted')

	args = p.parse_args()


	inf = open(args.infilename[0])
	outf = open(args.outfilename[0],'w')


	num = inf.readline()


	for i in range(int(num)):

		(r,t) = [long(a) for a in inf.readline().split()]


	
		
		outf.write('Case #%d: %d\n'%((i+1),comp(r,t)))
	

