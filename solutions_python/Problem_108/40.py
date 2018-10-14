T = int(raw_input());
for i in range(T):
   print "Case #%d:" % (i+1),;
   N = int(raw_input());
   Vine = [];
   for i in range(N):
      Vine.append( map(int, raw_input().split()) );
   D = int(raw_input());
   
   BestL = [0]*N;    # Best length reached for every vine;
   BestL[0] = Vine[0][0];
   TODO = [0];       # Start on vine #0;
   while len(TODO) != 0:
      start = TODO.pop(0);
      length= BestL[start];
      for j in range(N):
         if abs(Vine[j][0] - Vine[start][0]) <= length:
            # Can reach vine j
            # What distance will we have:
            dist = min(abs(Vine[j][0]-Vine[start][0]), Vine[j][1]);
            if dist > BestL[j]:
               BestL[j] = dist;
               TODO.append(j);

   #print BestL
   Possible = False;
   for V in range(N):
      if Vine[V][0] + BestL[V] >= D:
         Possible = True;
   if Possible:
      print "YES"
   else:
      print "NO"

#   print N, D
#   print Vine
