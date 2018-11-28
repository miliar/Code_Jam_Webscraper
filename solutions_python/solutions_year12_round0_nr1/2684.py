#!/usr/bin/env python
# encoding: utf-8
"""
SpeakingInTongues.py

Created by Katerina on 2012-04-14.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

T = 0
S = []
G = []
mapping = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}

def alphabet():
	return map(chr, range(97, 123))

def importSample():
	f = open('sample_input.txt', 'r')
	inp = f.read().split("\n")
	global T, S
	T = inp[0]
	S = inp[1:]
	return (T,S)

def importActualInput():
	f = open('A-small-attempt1.in.txt', 'r')
	inp = f.read().split("\n")
	global T, S
	T = inp[0]
	S = inp[1:]
	return (T,S)

def importSampleOutput():
	f = open('sample_output.txt', 'r')
	inp = f.read().split("\n")
	global G
	G = [v[9:] for v in inp]
	return G

def mapLanguages(normal, googlerese):
	global mapping
	m = zip(normal,googlerese)
	for pair in m:
		z = zip(pair[0],pair[1])
		for p in z:
			mapping[p[0]] = p[1]


def solveSample():
	f = open('solved_sample.txt', 'aw')
	o=[]
	oo=[]
	for t in S:
		for l in t:
			o.append(mapping[l])
		oo.append(''.join(o))
		o=[]
	counter = 1	
	for x in oo:
		print "Case #"+str(counter)+":",x
		f.write("Case #"+str(counter)+":"+" "+x+'\n')
		counter = counter+1

def solveProblem():
	f = open('solved_problem.txt', 'aw')
	o=[]
	oo=[]
	for t in S:
		for l in t:
			o.append(mapping[l])
		oo.append(''.join(o))
		o=[]
	counter = 1	
	for x in oo:
		print "Case #"+str(counter)+":",x
		f.write("Case #"+str(counter)+":"+" "+x+'\n')
		counter = counter+1
	

def main():
	importSample()
	importSampleOutput()
	mapLanguages(S,G)
	importActualInput()
	solveProblem()
	print T


if __name__ == '__main__':
	main()

