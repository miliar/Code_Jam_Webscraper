import math
import string

def self():
	N = 0
	N = int(sys.stdin.readline())
	i = 1
	while (i <= N):
		print "Case #"+str(i)+": ",
		i=i+1
		line = sys.stdin.readline()
		words = string.split(line) 
		if len(words) == 2:
			a = int(words[0])
			b = int(words[1])
			num = int(math.pow(2,a))
			if b%num==num-1:
				print "ON"
			else:
				print "OFF"
		else:
			break

if __name__ == "__main__":
	import sys
	self()
