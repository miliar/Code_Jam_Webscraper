from random import *

T = int(raw_input());
for i in range(T):
   print "Case #%d:" % (i+1),;
   [N, W, L] = map(int, raw_input().split());
   ri = map(int, raw_input().split());

   RI = []
   for e in ri:
      RI.append(e);
   
   NextRow = 0;
   
   TODO = range(N);
   xi = [0]*N;
   yi = [0]*N;
#   print TODO, ri
   X0 = 0;
   Y0 = 0;
   DONE = [];
   while len(TODO) != 0:
      R = max(ri);
      idex = ri.index(R);
      pers = TODO.pop(idex);
      R = ri.pop(idex);


      if X0==0==Y0:         # First person:
         xi[pers] = X0;
         yi[pers] = Y0;
         X0 += R;
         NextRow += R;
#         print "moo", R
      else:
         if X0 + R <= W:         # Fit on current row
            xi[pers] = X0+R;
            yi[pers] = Y0;
            X0 += 2*R
         else:
            X0 = 0;              # Start a new row
            Y0 = NextRow+R;
            xi[pers] = X0;
            yi[pers] = Y0;
            NextRow += R;
            X0 += R;

      #### Check
      x0 = xi[pers];
      y0 = yi[pers];
      r0 = R;
      Problem = False;
      for p in DONE:
         x1 = xi[p];
         y1 = yi[p];
         r1 = RI[p];
         if (x1-x0)**2 + (y1-y0)**2 < (r1+r0)**2:
            Problem = True; 
      while (Problem):
         x0 = int(W*random());
         y0 = int(L*random());
         Problem = False;
         for p in DONE:
            x1 = xi[p];
            y1 = yi[p];
            r1 = RI[p];
            if (x1-x0)**2 + (y1-y0)**2 < (r1+r0)**2:
               Problem = True;
      xi[pers] = x0;
      yi[pers] = y0;
         

      DONE.append(pers);
      
#      print pers, (xi[pers], yi[pers]);
#   print xi, yi
   for q in range(N):
      print xi[q], yi[q],
      if xi[q] > W or yi[q] > L:
         print "shitshitshit\n\n\n"
   print 
#      print TODO, ri
      

