f = open('in2')
cases = int(f.readline())

for case in range(cases):
   C, F, X = map(float, f.readline().split())

   
   t0 = 0.0
   v = 2.0 #speed
   ccc = 0.0  #current cookie count

   tend = (X-ccc)/v + t0 # at the current speed
   t_next_farm = t0 + (C-ccc)/v  
   tend_next_speed = t_next_farm + X/(v+F) 

   while (tend > tend_next_speed) :
      t0 = t_next_farm
      v = v+F
      ccc = 0.0
      tend = tend_next_speed

      t_next_farm = t0 + (C-ccc)/v  
      tend_next_speed = t_next_farm + X/(v+F)


#   print tend, t_next_farm, tend_next_speed
   print "Case #%d: %.7f"%(case+1, tend)

