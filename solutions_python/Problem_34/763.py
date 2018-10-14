#!/usr/bin/env python

import re

global dict,word_size,dict_size,test_num

def main():
	global test_num
	load_file()
	for i in range(1,test_num+1):
		try :
			eval(i,raw_input())
		except EOFError:
			break
	#debug()

def load_file():
	global dict,word_size,dict_size,test_num

	#grab and parse 1st line
	s = raw_input()
	sp = s.split()
	word_size = int(sp[0])
	dict_size = int(sp[1])
	test_num = int(sp[2])

	#fill dict
	dict = []
	for i in range(0,dict_size):
		dict.append(raw_input())

def debug():
	print "debug"
	global dict,word_size,dict_size,test_num
	print "l=",word_size,"\td=",dict_size,"\tn=",test_num
	print "dict = "
	for d in dict:
		print "\t",d

def eval(num,pattern):
	global dict
	found_num = 0

	pattern = pattern.replace('(','[').replace(')',']')
	p = re.compile(pattern)
	for d in dict:
		if p.match(d) != None:
			found_num += 1
	print "Case #%s: %d" % (num,found_num)


main()
