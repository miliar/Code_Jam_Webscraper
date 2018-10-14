def test(ca):
  ttc=100001
  time=0.0
  l=raw_input().split()
  c=float(l[0])
  f=float(l[1])
  x=float(l[2])
  a=100000.0
  rate=2.0
  while a <ttc:
    ttc=a
    a= (time +(x/ rate))
    time=time +(c/rate)
    rate =rate+f
  s=str(ttc)
  print "Case #" +str(ca) +": "+s

t =int(raw_input())
for testNum in range(1, t+1):
  test(testNum)
