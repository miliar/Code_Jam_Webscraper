from itertools import ifilter

tidies = []
for a in range(10):
 for b in range(a, 10):
  for c in range(b, 10):
   for d in range(c, 10):
    for e in range(d, 10):
     for f in range(e, 10):
      for g in range(f, 10):
       for h in range(g, 10):
        for i in range(h, 10):
         for j in range(i, 10):
          for k in range(j, 10):
           for l in range(k, 10):
            for m in range(l, 10):
             for n in range(m, 10):
              for o in range(n, 10):
               for p in range(o, 10):
                for q in range(p, 10):
                 for r in range(q, 10):
                  for s in range(r, 10):
                   for t in range(s, 10):
                    tidies.append(
                                  int(
                                      "".
                                      join(
                                           map(
                                               str,
                                               [a,b,c,d,e,f,g,h,i,j,k,
                                                l,m,n,o,p,q,r,s,t]
                                ))))
import time
print time.ctime()
for case in range(1, int(raw_input()) + 1):
    print "Case #%s:" % case,
    n = int(raw_input())
    print list(ifilter(lambda x: x <= n, tidies))[-1]
print time.ctime()


