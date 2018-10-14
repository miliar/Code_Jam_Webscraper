import os,sys

def mcd(x, y):
  while x != y:
    if x > y:
      x = x-y
    else:
      y = y-x
  return x

N=int(sys.stdin.readline())
for t in xrange(N):
        res = 0
        numbers=sys.stdin.readline().split()
        numbers= numbers[1:]
        numbers = [ int(x) for x in numbers ]
        unique = {}
        for n in numbers:
                unique[ n ] = 1
        numbers = unique.keys()
        numbers.sort()
        diff = {}
        for i in range(len(numbers)):
                if i > 0:
                        d = numbers[i] - numbers[i-1]

                        if d > 0:
                                diff[ d ] = 1
        diff = diff.keys()
        diff.sort()
        diff_GCD = diff[0]
        for i in range(len(diff)):
                if i > 0:
                        diff_GCD = mcd( diff_GCD, diff[i] )
        greatest = numbers[ -1 ]
        resto = greatest % diff_GCD
        delta = 0
        if resto > 0:
                delta = diff_GCD - resto
        res = str(delta).replace("L","")

        print "Case #%d: %s"% (t+1, res)
