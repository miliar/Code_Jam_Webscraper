def main():
  T = input()
  for t in xrange(T):
    input()
    ns = map(int,raw_input().split())
    a = 0
    for n in ns:
      a^=n
    if a:
      print "Case #%d: NO"%(t+1)
    else:
      print "Case #%d: %d"%(t+1,sum(ns)-min(ns))
      
main()
