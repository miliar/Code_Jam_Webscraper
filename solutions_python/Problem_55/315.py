import math
import string

def self():
	T = 0

	T = int(sys.stdin.readline())
	i = 1
	while (i <= T):
		print "Case #"+str(i)+":",
		i=i+1
		line = sys.stdin.readline()
		words = string.split(line) 
		g = []
		f = []
		total = 0
		if len(words) == 3:
			R = int(words[0])
			k = int(words[1])
			N = int(words[2])
		else:
			print "ERROR!"
			break
		line = sys.stdin.readline()
		words = string.split(line) 
		if len(words) == N:
			for word in words:
				g.append(int(word))
		else:
			print "ERROR!"
			break
		j = 0
		while j < R:
			riders = 0
			f = []
			while riders < k:
				if len(g)==0:
					break
				a = g.pop(0)
				new = a+riders
				if new > k:
					g.insert(0,a)
					break
				else:
					f.append(a)
					riders = new
			g.extend(f)
			total = total+riders
			j=j+1
		print total

if __name__ == "__main__":
	import sys
	self()
