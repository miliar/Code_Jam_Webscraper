#!/usr/bin/env python

import sys

def translate_word(word):
	dict={	'a':'y',
			'b':'h',
			'c':'e',
			'd':'s',
			'e':'o',
			'f':'c',
			'g':'v',
			'h':'x',
			'i':'d',
			'j':'u',
			'k':'i',
			'l':'g',
			'm':'l',
			'n':'b',
			'o':'k',
			'p':'r',
			'q':'z',
			'r':'t',
			's':'n',
			't':'w',
			'u':'j',
			'v':'p',
			'w':'f',
			'x':'m',
			'y':'a',
			'z':'q'}
	ret=''
	for c in word:
		ret+=dict[c]
	return ret

if __name__=='__main__':
	inpfile=open(sys.argv[1],'r')
	n=int(inpfile.readline())
	for i in range(0,n):
		inpline=inpfile.readline()
		words=inpline.split()
		print('Case #'+str(i+1)+':',end='')
		for w in words:
			print(' '+translate_word(w),end='')
		print('')
	inpfile.close()
