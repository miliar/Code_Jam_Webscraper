import string
import sys

inputfile = open('in.txt','r').read()
outputfile = open('out.txt','r').read()

inputfile = inputfile.replace(inputfile[0], '')

translate = {}

for i in range(len(outputfile)):
  translate[inputfile[i+1]] = outputfile[i]

