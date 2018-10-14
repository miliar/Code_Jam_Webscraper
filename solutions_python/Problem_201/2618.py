import sys

def stalls(n, k):
  stalls = ['0']
  stalls += ['.'] * n + ['0']


  for i in range(n):
    best = (n + 2, -1, -1)
    closest = 0
    for idx,j in enumerate(stalls):
      #print idx, j, best, closest
      if j == '0': continue
      ls = rs = 0
      cur = idx - 1
      while cur > 0:
        if stalls[cur] == '0': break
        ls += 1
        cur -= 1
      #print ls
      if ls < closest: continue
      cur = idx + 1
      while cur < n + 1:
        if stalls[cur] == '0': break
        rs += 1
        cur += 1
      #print rs
      if rs < closest: continue
      if min(ls, rs) > closest \
         or ls == closest and rs > max(best[1], best[2]) \
         or rs == closest and ls > max(best[1], best[2]):
        closest = min(ls, rs)
        best = (idx, ls, rs)
    stalls[best[0]] = '0'
    #print 'n = ' + str(i+1) + ' ls =' + str(best[1]) + ' rs = ' + str(best[2])    
    if k == i + 1:
      return (max(best[1], best[2]), min(best[1], best[2]))
    


if __name__ == '__main__':
  tests = input()
  for i in range(tests):
    x,y = map(int,sys.stdin.readline().split())
    res = stalls(x,y)
    print "Case #" + str(i + 1) +": " + str(res[0]), str(res[1])

      

