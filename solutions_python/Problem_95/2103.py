#! /usr/bin/env python

import operator
from sys import stdin

in1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq"
out1 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz"

sample = "ejp mysljylc kd kxveddknmc re jsicpdrysi"


def getInput():
	raw = stdin.readlines()
	for x in range(0, len(raw)):
		raw[x] = raw[x].replace('\n', '')
	return raw

def makeMap(input_str, output_str):
	mymap = {}
	for x,y in zip(input_str, output_str):
		if(x != " "):
			mymap[x] = y
	return mymap

def googler2english(input_str):
	mymap = makeMap(in1, out1)
	ret_str = ""
	for x in input_str:
		if x != ' ':
			ret_str = ret_str + mymap[x]
		else:
			ret_str = ret_str + " "
	return ret_str

def main():
	myinput = getInput()
	bound = int(myinput[0])
	for x in range(1, bound + 1):
		print "Case #%d: %s" % (x, googler2english(myinput[x]))
	

if __name__ == "__main__":
	main()
