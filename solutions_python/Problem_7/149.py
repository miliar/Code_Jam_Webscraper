#! /usr/bin/env python

q = input()
for i in range(q):
   XX, YY = [], []
   n, A, B, C, D, x0, y0, M = map(int,raw_input().split(' '))
   X = x0 
   Y = y0
   count = 0
   XX.append(X)
   YY.append(Y)
   for j in range (n-1):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      XX.append(X)
      YY.append(Y)
   
   for k in range(len(XX)):
      for w in range(k+1,len(XX)):
         for l in range(w+1,len(XX)):
            xc = (XX[k] + XX[w] + XX[l]) / 3;
            yc = (YY[k] + YY[w] + YY[l]) / 3;
            if ((XX[k] + XX[w] + XX[l]) % 3) == 0 and ((YY[k] + YY[w] + YY[l]) % 3) == 0:
               count += 1

   print "Case #"+str(i+1)+": "+str(count)
