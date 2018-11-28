
def max_diff(N, A,B):
  A = sorted(A, reverse=True)
  B = sorted(B, reverse=True)

  counter = 0
  i = 0
  j = 0

  for t in xrange(N):
   if A[i] > B[j]:
     counter += 1
     i += 1
   else:
     i += 1
     j += 1 

  return counter

def optimial_war(N, noami, ken):
  return max_diff(N, noami, ken)

def optiaml_deceitful_war(N, noami, ken):
  return N - max_diff(N, ken, noami)

if __name__ == '__main__':
   T = int(raw_input())

   for i in xrange(1,T+1):
     N = int(raw_input())
     noami = list(float(x) for x in raw_input().split())
     ken = list(float(x) for x in raw_input().split())


     opt_war = optimial_war(N, noami, ken)
     opt_dec = optiaml_deceitful_war(N, noami, ken)

     print "Case #%s: %s %s" % (i, opt_dec, opt_war)
     
