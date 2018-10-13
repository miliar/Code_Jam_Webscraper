for c in xrange(int(raw_input())):
  inp=map(int,raw_input().split())
  N=inp[0]
  S=inp[1]
  p=inp[2]
  nonsmin=max(p*3-2,p+0+0)
  smin=max(p*3-4,p+0+0)
  easy=0
  maybe=0
  for i in inp[3:]:
    if i>=nonsmin:
      easy+=1
    elif i>=smin:
      maybe+=1
  print "Case #"+str(c+1)+":",easy+min(S,maybe)
