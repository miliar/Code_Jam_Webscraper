from bigfloat import *
def paintReq(r, p):
   return int(floor(0.25*(sqrt(8*p + pow(2*r-1, 2, precision(100)), precision(100)) - 2*r + 1)))

number_of_test_cases = int(raw_input())
for test_i in range(1, number_of_test_cases + 1):
   (r, p) = map(int, raw_input().split())
   print "Case #%s: %s" % (test_i, paintReq(r, p))