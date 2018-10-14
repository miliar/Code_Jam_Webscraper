import sys
 
def tidy(s):
  if len(s) == 1: return s 

  a = [int(x) for x in list(s)]

  # review from right to left fixing as we move left
  #        12329238..292329832
  #                         **
  #                         <<
  #

  pos = len(a)-2
  while pos >= 0:
      if a[pos] > a[pos+1]:
          a[pos] -= 1
          pos2 = pos+1
          while pos2 < len(a):
             a[pos2] = 9
             pos2 += 1

      pos -= 1

  # remove initial 0s
  while len(a) > 0 and a[0] == 0:
     a = a[1:]

  return ''.join([str(x) for x in a])

# main()
 
for tc in xrange(1, int(sys.stdin.readline())+1):
    numero = sys.stdin.readline().strip()
    bkp = numero
 
    tidyit = tidy(numero)
    print 'Case #%d: %s' % (tc, tidyit)
