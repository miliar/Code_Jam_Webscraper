#!/usr/bin/python

import sys;

if len(sys.argv) == 2:
  with open(str(sys.argv[1]), 'r') as f:
    T = int(f.readline());

    for t in xrange(T):
      N = int(f.readline());

      naomi = sorted(str(f.readline()).rstrip().split(' '));
      ken = sorted(str(f.readline()).rstrip().split(' '));

      ken_w = list(ken);

      W = 0;
      for i in xrange(len(naomi)):
        j = 0;
        while(naomi[i] > ken_w[j]):
          j += 1;
          if j == len(ken_w):
            break;

        if j == len(ken_w):
          W += 1;
          del ken_w[0];
        else:
          del ken_w[j];

      DW = 0;
      while len(naomi) != 0:
        i = len(naomi)-1;
        if ken[-1] > naomi[i]:
          j = len(ken)-1;
          while ken[j] > naomi[i]:
            j -= 1;
            if j == -1:
              break;
          j += 1;

          del ken[j];
          del naomi[0];
        else:
          i = 0;
          while ken[0] > naomi[i]:
            i += 1;

          del ken[0];
          del naomi[i];
          DW += 1;

      print "Case #%d: %d %d" % (t+1, DW, W);





