def run(callback):
 import re, sys
 fptr = open(sys.argv[1])
 for i in range(1,int(fptr.readline())+1):
  print "Case #" + str(i) + ": " + callback(fptr.readline().split(' '))
