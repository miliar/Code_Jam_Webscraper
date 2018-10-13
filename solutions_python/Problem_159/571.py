def solveY(a):
   s = 0
   for i in range(len(a) - 1):
      if (a[i+1] < a[i]):
         s += a[i] - a[i+1]
   return s
   
def solveZ(a):
   def maxdist(a):
      dist = 0
      for i in range(len(a) - 1):
         dist = max(dist, a[i] - a[i+1])
      return dist
   dist = maxdist(a)
   s = 0
   for x in a[:len(a)-1]:
      s += min(dist, x)
   return s
   
def main():
   T = int(raw_input())

   for case_n in range(1,T+1):
      N = int(raw_input())
      a = []
      line = raw_input().split(' ')
      for i in range(N):
         a.append(int(line[i]))
      
      print "Case #%d: %d %d" % (case_n, solveY(a), solveZ(a))


main()
