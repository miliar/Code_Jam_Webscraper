#!/usr/bin/python

import sys;

if len(sys.argv) == 2:
  with open(str(sys.argv[1]), 'r') as f:
    N = int(f.readline());

    for n in xrange(N):
      line = str(f.readline()).rstrip().split(' ');
      C = float(line[0]);
      F = float(line[1]);
      X = float(line[2]);

      lastTc = C/2.0;
      lastTx = X/2.0;
      K = 1;
      while(True):
        Tc = lastTc + C/(2.0 + K*F);
        Tx = lastTc + X/(2.0 + K*F);

        if (Tx > lastTx):
          print "Case #%d: %.7f" % (n+1, round(lastTx, 7));
          break;
        else:
          lastTc = Tc;
          lastTx = Tx;
          K += 1;
