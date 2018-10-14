#!/usr/local/bin/python

import sys;


cases = int(sys.stdin.readline());
for i in xrange(cases):
   numbers = sys.stdin.readline();
   items = sys.stdin.readline();
   foo = items.split();

   intList = [];

   for j in xrange(len(foo)):
      intList.append(int(foo[j]));

   intList.sort(reverse=True);
   bits = [0]*25;

   for j in xrange(len(intList)):
      binaryStringReverse = bin(intList[j])[::-1];
      for k in xrange(len(binaryStringReverse) - 2):
         if (binaryStringReverse[k] == '1'):
            bits[k] += 1;

   flag = 0;
   for j in xrange(len(bits)):
      if (bits[j] % 2):
         flag = 1;

   k = i+1;
   if (flag):
      print "Case #%d: NO" %k;
   else:
      total = sum(intList) - intList[len(intList)-1];
      print "Case #%d: %d" % (k, total);

