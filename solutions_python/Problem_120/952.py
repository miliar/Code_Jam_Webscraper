#!/usr/bin/python2.7 -tt
import sys
def main():
	filename = sys.argv[1]
	base = '/Users/arjunrao/Downloads/codejam/'
	f = open(base+filename+'.in','r')
	w = open(base+filename+'.out','w')
	ntc = int(f.readline())
	for i in range(ntc):
		sl = f.readline().split()
		r = int(sl[0])
		t = int(sl[1])
		fl = -1
		total = 0
		lines = 0;
		j = r
		while True:
			total = total + j * j * fl
			if total > t:
				break
			if total == t:
				lines+=1
				break
			if fl > 0:
				lines+=1
			fl *= -1
			j+=1
			if j == 1000000000000000000000:
				break
		w.write('Case #'+str(i+1)+': '+str(lines)+'\n')

if __name__ == '__main__':
	main()
