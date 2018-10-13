import sys;
import math;
def main():
	tc=int(raw_input());
	for c in range(tc):
		rt=map(int,raw_input().strip().split(" ",2));
		r=rt[0];
		t=rt[1];
		counter=0;
		j=r+1;
		while True:
			val=2*j-1;
			if val <=t:
			        counter=counter+1;
			        t=t-val;
				j=j+2;
			else: break;
		print "Case #%s: %s" %(str(c+1),str(counter))

if __name__=="__main__":main();
