N = int(raw_input())
orig = 'welcome to code jam'
n = 0
def count_seq(po, target, pt):
  if len(orig)==po:
    global n
    n+=1
  else: # find next positions
    nc = orig[po]
    npt = target.find(nc, pt)
    while npt>-1:
      count_seq(po+1, target, npt+1)
      npt = target.find(nc, npt+1)
    
for _ in range(N):
  target = raw_input()
  n = 0
  count_seq(0, target, 0)
  print 'Case #%d: %04d' %(_+1, n)
