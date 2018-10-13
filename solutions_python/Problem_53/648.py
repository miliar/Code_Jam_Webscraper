ON = "ON"
OFF = "OFF"

def snapperChainSmall(n,k):
   n = 1 << n
   k = k % n
   if (n - 1 == k): return ON
   else: return OFF

count = input()
for i in range(1, count + 1):
  (n, k) = map(int, raw_input().split(' '))
  print "Case #%s: %s" % (i, snapperChainSmall(n,k))

