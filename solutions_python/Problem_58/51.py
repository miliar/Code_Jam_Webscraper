ww=0

def rjA(A,B):
   global ww
   #print "A-",A, B
   if A==B:
      return False
   if B==0:
      return True
   x=False
   y=False
   if A%B>0 and A%B<A:
      x= rjB(B, A%B)
   if A%B+B<A:
      y= rjB(A%B+B,B)
   return x or y
     
         

def rjB(A,B):
   #print "B-",A, B
   if A==B:
      return True
   if B==0:
      return False
   x=True
   y=True

   if A%B>0 and A%B<A:
      x = rjA(B, A%B)

   if A%B+B<A:
      y = rjA(A%B+B,B)

   return x and y
      

zad = open("C-small-attempt2.in").read()
z = zad.split('\n')

o = open("out.txt",'w')

try:
   for l in xrange(1,len(z)):
      znj = z[l].split()
      
      A1 = int(znj[0])
      A2 = int(znj[1])
      B1 = int(znj[2])
      B2 = int(znj[3])
      #print A1,A2,B1,B2
      ww=0
      for A in xrange(A1,A2+1):
         for B in xrange(B1,B2+1):
            if A>B:
               F = rjA(A,B)
            else:
               F = rjA(B,A)
            if F:
               ww+=1
         
      #print "Case #%d: %d" % (l,ww) 
      o.write("Case #%d: %d\n" % (l,ww) )
except:
   print "nana"
   
print "ok"