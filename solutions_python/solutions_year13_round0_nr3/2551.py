def fair(n):
   l = list(str(n))
   return l == list(reversed(l))

from gmpy import is_square as square
from gmpy import sqrt
def test():
   assert fair(6)
   assert fair(121)
   assert not fair(49)
   assert not square(10)
   assert square(49)

number_of_test_cases = int(raw_input())
for test_i in range(1, number_of_test_cases + 1):
   (start, end) = map(int, raw_input().split())
   fas_count = len([ 1 for n in range(start, end + 1)
                     if fair(n) and square(n) and fair(int(sqrt(n))) ])  
   print "Case #%s: %s" % (test_i, fas_count)