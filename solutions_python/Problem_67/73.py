# Google code jam round 2, problem B

from numpy import *

FILE = open("C-small.in","r");

N = 200;

def Iterate(List):
   OldArr = zeros(N*N, int);
   NewArr = zeros(N*N, int);
   for k in range(len(List)):
      OldArr[List[k]] = 1;
   NewList = [];
#   print List, NewList
   for b in List:
      x = b/N;    y = b%N;

      if ((x > 0) and (y > 0)):
         if OldArr[b+1] == 0:
            if (OldArr[b+1-N] == 1):
               NewArr[b+1] = 1;
               NewList.append(b+1)
               
      if (y > 0):
         if (OldArr[b-1] == 1):
            NewArr[b] = 1;
            NewList.append(b);
      if (x > 0):
         if (OldArr[b-N] == 1):
            if (NewArr[b] == 0):
               NewArr[b] = 1;
               NewList.append(b);


   return NewList;
         


def Solve(RECS, R):
   Bac = [];
   for k in range(R):
      for x in range(RECS[k][0], RECS[k][2]+1):
         for y in range(RECS[k][1], RECS[k][3]+1):
            Bac.append(N*x+y);

   T = 0;
   while len(Bac) > 0:
#      print Bac;
      Bac = Iterate(Bac);
      T += 1;

   return T;


C = int(FILE.readline());
for k in range(C):          # Each of the N cases:
   R = int(FILE.readline());
   RECS = [];
   for q in range(R):
      RECS.append(map(int, FILE.readline().split()));
   print "Case #%d:" %(k+1),
   print Solve(RECS, R);
