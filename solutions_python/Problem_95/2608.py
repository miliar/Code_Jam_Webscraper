#!/usr/bin/env python

#
# Problem 1. Googlerese
#

def main():
	googlerese = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
			'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f',
			'm', 'a', 'q']
			
	N = int(raw_input())

	for i in range(N):
		in_str = raw_input()
		out_str = ""
		
		for s in in_str:
			if ord(s) >= 97 and ord(s) <= 125:
				out_str += googlerese[ord(s) % 97]
			else:
				out_str += s
				
		print "Case #%d: %s" % (i+1, out_str)
	
	
if __name__ == '__main__':
	main()
