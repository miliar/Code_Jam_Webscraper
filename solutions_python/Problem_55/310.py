import numpy

def gendi(arr, k):
   di = dict()
   l = len(arr)
   for i in xrange(l):
      zarada = arr[i]
      shift = 1
      for j in xrange(i+1,l+l):
         if zarada+arr[j%l]<=k and shift<l:
            zarada = zarada + arr[j%l]
            shift+=1
         else: break
      di[i] = (zarada, shift)
   return di
         

zad = open("C-small-attempt0.in").read()
z = zad.split('\n')

o = open("out.txt",'w')

try:
   for l in xrange(1,len(z),2):
      znj = z[l].split()
      zn = z[l+1].split()
      
      R = int(znj[0])
      k = int(znj[1])
      N = int(znj[2])
      a = [int(p) for p in zn]
      b = numpy.array(a)
      
      di = gendi(b, k)
      p = 0
      c = 0
      while R:
         R-=1
         p = p%N
         c += di[p][0]
         p += di[p][1]
         
      #print "Case #%d: %d\n" % ((l+1)/2,c) 
      o.write("Case #%d: %d\n" % ((l+1)/2,c) )
except:
   print "nana"
   
print "ok"