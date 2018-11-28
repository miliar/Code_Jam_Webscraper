#!/usr/bin/python
import sys
def isTidy(n):
	if(len(n) == 1):
		return True
	tidy = True
	i = 1
	last_diget = n[0]
	while (tidy and i < len(n)):
		tidy = (int(last_diget) <= int(n[i]))
		last_diget = n[i]
		i+=1
	return tidy
def getTidy(n):
	while True:
		if isTidy(str(n)):
			return n
		n = n-1

def main():
	f = open(sys.argv[1], 'r')
	lines = f.readlines()
	f.close()
	t = int(lines[0])
	for i in range(0, t):
		print "Case #%d: %d"%(i+1, getTidy(int(lines[i+1])))



if __name__ == "__main__":
	main()
