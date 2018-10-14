#!/usr/bin/python

import sys

def main():
	
    f = open(sys.argv[1]).read().splitlines()
    n = int(f[0])
    count = 0
    i = 1
    while count < n:
   		
   		mole, number = f[i].split(' ')
   		i = i + 1
   		moles = f[i].split(' ')
   		i = i + 1
   		moles = map(int, moles)
   		moles.sort()
   		ans = 0
   		s = int(mole)
   		num = []
   		totalmoles = len(moles)
   		for m in moles:
			if s == 1:
   				break
   			num.append(ans + totalmoles - (moles.index(m)))
   			if s <= m:
   				while s <= m:
   					ans = ans + 1
   					s = s + s - 1
   			s = s + m
   		num.append(ans)
   		if s == 1:
   			finalans = totalmoles
   		else:
   			finalans = min(num)
   		count = count + 1
   		print "Case #" + str(count) + ": " + str(finalans)

if __name__=='__main__':
    main()
