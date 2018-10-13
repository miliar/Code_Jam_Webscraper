#!/usr/bin/python
# -*- coding: utf-8 -*-
#Alien language for Google Code Jam 2009, by Alan Fischer e Silva

import sys
import math

def print_anagrama(line, dictionary, L, n):
	K = 0
	char_list = []
	i = 0
	while i < len(line):
		if line[i] == '(':
			chars = ''
			j = i + 1
			while j < len(line):
				if line[j] != ')':
					chars = chars + line[j]
					j = j + 1
				else:
					char_list.append(chars)
					i = j + 1
					break
		else:
			char_list.append(line[i])
			i = i + 1

	for word in dictionary:
		i = 0
		j = 0
		for char in word:
			for c in char_list[i]:
				if c == char:
					j = j + 1
			i = i + 1
		if j == int(L): K = K + 1

	print "Case #%d: %s" % (n, K)

if len(sys.argv) <> 2:
	print "Correct usage: alien <filename>"
	exit(1)

f = open(sys.argv[1], 'r')

Ns = f.readline()
Ns= Ns.rstrip('\n')
L, D, N = Ns.split(' ')

i = 1
n = 1
dictionary = []
for line in f:
	line = line.rstrip('\n')
	if i <= int(D):
		dictionary.append(line)
		i = i + 1
	else:
		print_anagrama(line, dictionary, L, n)
		n = n + 1