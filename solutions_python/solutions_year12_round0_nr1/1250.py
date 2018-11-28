import sys

if (len(sys.argv) != 2):
  print "Require 1 input file as argument"
  exit(1)
  
inputFile = open(sys.argv[1])
N = int(inputFile.readline())

dictionary = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

for i in range(N):
  inputTXT = inputFile.readline()[:-1]
  outputTXT = ""
  for j in range(len(inputTXT)):
    outputTXT += dictionary[inputTXT[j]]
  print "Case #%d: %s" % (i+1, outputTXT)

inputFile.close()
