T = input()

for t in range(1,T+1):
  l,size = map(int,raw_input().split())
  files = map(int,raw_input().split())
  sort = sorted(files, reverse=True)
  packs = 0
  while len(sort)!=0:
    packs += 1
    big = sort[0]
    rest = size-big
    l = 0
    r = len(sort)-1
    if len(sort)>1 and sort[r]<=rest:
      while r-l>1:
        m = (l+r) / 2
        if sort[m]<=rest:
          r=m
        else:
          l=m
      del sort[r]
    del sort[0]
  print "Case #"+str(t)+": "+str(packs)
