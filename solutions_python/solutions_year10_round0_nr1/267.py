def run(fptr, callback):
 import re
 for i in range(1,int(fptr.readline())+1):
  print "Case #" + str(i) + ": " + callback(fptr.readline().split(' '))
