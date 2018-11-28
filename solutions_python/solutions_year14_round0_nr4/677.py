for T in xrange(input()):
 n = input()
 a = sorted(map(float,raw_input().split()))
 b = sorted(map(float,raw_input().split()))
 
 #print a;print b


 t = (list(a),list(b))
 

 ans = 0
 Ans = 0
 while len(a)>0:
  if a[-1]>b[-1]:
   a.pop(-1)
   b.pop(-1)
   Ans+=1
   if len(b)==0 or len(a) == 0: break
  else:
   b.pop(-1)
   if len(b)==0: break

 a,b = t
 
 while len(a)>0:
  if a[0]<b[0]:
   a.pop(0)
   b.pop(0)
   if len(b)==0 or len(a) == 0: break
  else:
   b.pop(0)
   if len(b)==0: break

 ans = len(a)
 print("Case #%d: %d %d" % (T+1,Ans,ans))