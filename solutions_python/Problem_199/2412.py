import numpy
import math
from random import randrange

def pancakes():
	cases = int(input())
	for case in range(0,cases):
		pancake = str(input()).split()
		K = int(pancake[1])
		pancake = pancake[0]
		flips = 0
		boolCake = []
		for i in pancake:
			if(i=='+'):
				boolCake.append(True)
			else:
				boolCake.append(False)
		for i in range(0,len(boolCake)):
			if(not boolCake[i]):
				if(i+K > len(boolCake)):
					print("Case #" + str(case+1) + ": IMPOSSIBLE")
					i = 9999
					break
				else:
					flips += 1
					for m in range(i,i+K):
						boolCake[m] = not boolCake[m]
		if(i!=9999):
			print("Case #" + str(case+1) + ": " + str(flips))

pancakes()
