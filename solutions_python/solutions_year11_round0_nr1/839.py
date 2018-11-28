#!/usr/bin/python
import sys

argv = sys.argv
input = open(argv[1]).read().split("\n")
n = int(input.pop(0))

for i in xrange(n):
       array = input.pop(0).split(" ")
       num = int(array.pop(0))
       hash = {"B":1,"O":1}
       time = 0
       buf = 0
       for j in xrange(0,num*2,2):
               if j == 0:
                       time = abs(int(array[1]) - hash.get(array[0]))+1
                       buf = time
               elif array[j] == array[j-2]:
                       tmp = abs(int(array[j+1]) - hash.get(array[j])) + 1
                       buf += tmp
                       time += tmp
               elif array[j] != array[j-2]:
                       tmp = abs(int(array[j+1]) - hash.get(array[j]))
                       if buf >= tmp:
                               time += 1
                               buf = 1
                       else:
                               time += tmp + 1 - buf
                               buf = tmp + 1 - buf
               hash.update({array[j]:int(array[j+1])})
       print "Case #%s: %s" % (i+1,time)
