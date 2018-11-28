for Pr in xrange(1, input()+1):
   D, N=[int(x) for x in raw_input().split()]
   d, v=[], []
   for i in xrange(N):
     c=[int(x) for x in raw_input().split()]
     d.append(c[0])
     v.append(c[1])
   d_sort=[k for k in d]
   d_sort.sort()
   v_sort=[]
   for k in d_sort:
     v_sort.append(v[d.index(k)])
   d,v=d_sort, v_sort
   curv=v[0]
   d_ok, v_ok=[d[0]], [v[0]]
   for i in xrange(1, N):
     if v[i]<curv:
       d_ok.append(d[i])
       v_ok.append(v[i])
       curv=v[i]
   d, v=d_ok, v_ok
   N=len(d)
   d1, v1=d[0], v[0]
   T=0
   for i in xrange(1, N):
     t=float(d1-d[i])/(v[i]-v1)
     dd=d1+v1*t
     
     if D<=dd:
       break
     else:
       d1=dd
       v1=v[i]
       T+= t
       
   T+= (D-d1)/float(v1)
   solve=D/T
   print 'Case #%d: %f'%(Pr, solve)
   
   
   
   
   
   