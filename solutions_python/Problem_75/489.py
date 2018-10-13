#!/usr/bin/python

import sys

def main ():
	args = sys.argv[1:]
	
	f = open(args[0])
	ncases = int(f.readline())
	
	for i in xrange(0, ncases):
		info = f.readline().rsplit()
		
		ncombos = int(info.pop(0))
		combos  = map(lambda s: (s[:2], s[2]), info[:ncombos])
		info    = info[ncombos:]
		
		nopposeds = int(info.pop(0))
		opposeds  = info[:nopposeds]
		info      = info[nopposeds:]
		
		#linvokation = int(info.pop(0))
		invokation  = info.pop()
		r = []
		
		for c in invokation:
			r.append(c)
			
			if len(r) == 1:
				continue
			else:
				makescombo = False
				for x in combos:
					if c in x[0] and r[-2] in x[0].replace(c, "", 1):
						r[-2] = x[1]
						r = r[:-1]
						makescombo = True
						break
				
				if makescombo:
					continue
				
				for o in opposeds:
					if c in o and o.replace(c, "", 1) in r[:-1]:
						r = []
						break
				if r == []:
					continue
		
		print "Case #"+str(i+1)+":", str(r).replace("'","")

if __name__ == "__main__":
	main ()
