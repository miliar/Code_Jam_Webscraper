# Broken when:
# P_D is not 100 but P_G is
# P_D is not 0 but P_G is
# When there exists no number between 1 and N such that n * P_D is a multiple of 100
import fractions

f = open('A-large.in', 'r')
cases = int(f.next())
for i in xrange(cases):
  N, P_D, P_G = [int(x) for x in f.next().split()]
  
  if (P_G == 100 and P_D != 100) or (P_G == 0 and P_D != 0) or (100 / fractions.gcd(100, P_D) > N):
    print "Case #%d: Broken" % (i + 1)
  else:
    print "Case #%d: Possible" % (i + 1)