#!/usr/bin/python2

#inf = open("A-small-attempt0.in");
inf = open("A-large.in");

r4 = range(4);

T=int(inf.readline());
for t in xrange(T):
   ld=[True, True]
   rd=[True, True]
   up=[ld+ld,ld+ld]
   le=[True, True]
   xw = False;
   ow = False;
   em = False;
   for i in r4:
      ln = inf.readline();
      le=[True, True]
      for j in r4:
         c = ln[j]
         if c=='.':
            em=True;
            for k in [0,1]:
               le[k]=False;
               up[k][j]=False;
               if i==j: ld[k]=False;
               if i==3-j:rd[k]=False;
         elif c=='X':
            k=1;
            le[k]=False;
            up[k][j]=False;
            if i==j: ld[k]=False;
            if i==3-j:rd[k]=False;
         elif c=='O':
            k=0
            le[k]=False;
            up[k][j]=False;
            if i==j: ld[k]=False;
            if i==3-j:rd[k]=False;
      if le[0]:xw=True;
      elif le[1]:ow=True;
   inf.readline();
   for j in r4:
      if up[0][j]:xw=True;
      if up[1][j]:ow=True;
   print "Case #"+str(t+1)+":",
   if xw or ld[0] or rd[0]:
      print("X won");
   elif ow or ld[1] or rd[1]:
      print("O won");
   elif em:
      print("Game has not completed");
   else:
      print("Draw");

inf.close();
