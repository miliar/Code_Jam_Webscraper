from itertools import permutations

def coin(ordert, P):
   prison = [1]*P
   coins = 0
   order = list(ordert)

#   print order, 

   while order:
      r = order.pop()-1
      prison[r] = 0
      
      for i in xrange(r+1, P):
         if prison[i]:
            coins += 1
         else:
            break
      
      for i in xrange(r-1, -1, -1):
         if prison[i]:
            coins += 1
         else:
            break

 #  print coins
   return coins




f = open('file.txt')
N = int(f.readline())

n = 0
while n != N:
   n += 1

   P, Q = map(int, f.readline().split())
   release = map(int, f.readline().split())

   print "Case #%d: %d" % (n, min(coin(order, P) for order in permutations(release)))

f.close()

