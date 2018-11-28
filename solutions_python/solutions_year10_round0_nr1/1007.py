import sys;
import numpy as np;
import pdb;

def main(s):
	# passed on N and K 
	[N, K] = np.array(s.split(), dtype = np.int32);
	elec_supp = np.binary_repr(2**(int(N)-1), N);#1= R
	elec_supp = np.array([int(i) for i in elec_supp  ], dtype= np.int32);
	state = np.binary_repr(0, N);#1=ON
	state = np.array([int(i) for i in state], dtype= np.int32);
	# K snaps later...
	for i in range(K):
		state_new = np.bitwise_xor(state,elec_supp);
		state= state_new;
		for j in xrange(1,N,1):
			elec_supp[j]= np.bitwise_and(state[j-1],elec_supp[j-1]);
		#print 'S::',state;	
		#print 'ES::',elec_supp
	return np.bitwise_and(state, elec_supp);
if __name__ == '__main__':

	print "I/P file pls:"
	file = sys.stdin.readline()
	f = open(file.strip(),"r");
	f2 = open("./output","w")

	
	# read the I/p now....
	s = f.readline();
	numcases = int(s.strip());
	for i in range(numcases):
		state = main(f.readline());
		#pdb.set_trace();
		#print 'state =',state
		if np.bitwise_and(state[len(state)-1],1):
			f2.writelines('Case #'+str(i+1)+': ON\n');
		else:
			f2.writelines('Case #'+str(i+1)+': OFF\n') 
			  
	f2.close()
