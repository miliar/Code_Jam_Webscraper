def main():
  T = input()
  for t in xrange(T):
    N,PD,PG = map(int,raw_input().split())
    print "Case #%d:"%(t+1),
    if (PG == 100 and PD != 100) or (PG==0 and PD != 0):
      print "Broken"
      continue
    a,b = PD,100
    while b:
      a, b = b, a%b
    c = 100/a
    if c <= N:
      print "Possible"
    else:
      print "Broken"
main()
