#!/usr/bin/env python

import urllib, urllib2, cookielib
import re #biblioteca que procura expressao regular
import os #roda o programa em C que trata a entrada gerada
import string

from sys import argv

entrada = open('B-small-attempt1.in', 'r')
saida = open('B-small-attempt1.out', 'w')

number = int(entrada.readline())
sentences = ''

# number of tests
for i in range(number):
	sentences += "Case #" + str(i+1) + ': ' 
	# for each test
	j = entrada.readline()
	numbers = string.split(j, ' ')
	count = 0
	googlers = int(numbers[0])
	surpriz = int(numbers[1])
	p = int(numbers[2])
	if p == 0:
		min_no_surprise = 0	
		min_surprise = 0
	elif p == 1:
		min_no_surprise = 1
		min_surprise = 1
	else:
		min_no_surprise = 3*p - 2
		min_surprise = 3*p - 4
	for i in range(3, len(numbers)):
		if int(numbers[i]) >= min_no_surprise and p <= 10:
			count += 1
		elif int(numbers[i]) >= min_surprise and surpriz > 0 and p <= 10:
			count += 1
			surpriz -= 1
	sentences += str(count)
	if i != number - 1:
		sentences += '\n'
saida.write(sentences)

entrada.close()	
saida.close()