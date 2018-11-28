#!/usr/bin/python
import sys

def mainfunc():
	f = open("input.txt", "r")
	i = int(f.readline().strip())
	j = 0;
	gmap = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f',
		'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l',
		'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 
		'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 
		'a':'y', 'q':'z', ' ':' ', '\n':'\n'}
	while (j < i):
		gl = list(f.readline())
		el = [gmap[x] for x in gl]
		print "Case #%d: %s" % (j+1, "".join(el)),
		j += 1
	
if __name__ == "__main__":
	mainfunc()
