import math
import string
import fractions

def self():
	N = 0
	N = int(sys.stdin.readline())
	i = 1
	while (i <= N):
		print "Case #"+str(i)+": ",
		i=i+1
		line = sys.stdin.readline()
		words = string.split(line) 
		if len(words) == 0:
			break
		elif len(words) == int(words[0])+1:
			j = 2
			first = int(words[1])
			div = abs(first - int(words[j]))
			while True:
				if j == int(words[0]):
					break
				j=j+1
				div = abs(fractions.gcd(first - int(words[j]), div))
				if div == 1:
					break
			mod = first%div
			if mod == 0:
				print "0"
			else:
				print (div-mod)
		else:
			break

if __name__ == "__main__":
	import sys
	self()
