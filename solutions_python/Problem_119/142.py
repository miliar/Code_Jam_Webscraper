from sys import stdout

keys = []
require = []
existing = []
res = []
deleted = []

def add_list(l1, l2):
  for i in range(len(l2)):
    l1[i] += l2[i]

def minus_list(l1, l2):
  for i in range(len(l2)):
    l1[i] -= l2[i]

def smaller_list(l1, l2):
  if len(l1) == 0:
    return True
  for i in range(len(l2)):
    if l1[i]>l2[i]:
      return False
  return True

def decide(t, trea, K,N):
  global keys, require, existing, deleted, res, finalRes
  if(len(res) == N):
    return res
  for j in range(N):
    # check existing 
    if existing[t[j]] < require[t[j]]:
     #   print j, existing[t[j]], require[t[j]]
      return []

    if not deleted[j] and keys[t[j]]>0:
    # check unique
      if require[t[j]] == 1 and keys[t[j]] == 1:
        deleted[j] = True
        res.append(j)
        keys[t[j]] -= 1
        require[t[j]] -= 1
        existing[t[j]] -= 1  
        add_list(keys, trea[j])
        a = decide(t, trea, K,N)
        if len(a) is not 0:
          return res 
        minus_list(keys, trea[j])
        existing[t[j]] += 1
        require[t[j]] += 1 
        keys[t[j]] += 1
        res.pop()
        deleted[j] = False
      else: 
        aj = sum([trea[k][t[j]] for k in range(N) if t[j] is not t[k]])
        aj += trea[j][t[j]]
     # if res == [1, 2, 3, 4]:
     #   print j, t[j], require[t[j]], aj, keys[t[j]]
      #print j, aj, require[t[j]], keys[t[j]]
        if aj+keys[t[j]]-1 > 0 or require[t[j]] == 0:
          deleted[j] = True
          res.append(j)
          keys[t[j]] -= 1
          require[t[j]] -= 1
          existing[t[j]] -= 1
          add_list(keys, trea[j])
          a = decide(t, trea, K,N)
          if len(a) is not 0:
            return res 
          minus_list(keys, trea[j])
          existing[t[j]] += 1
          require[t[j]] += 1 
          keys[t[j]] += 1
          res.pop()
          deleted[j] = False
  return []
                     
def solve():
  global keys, require, existing, deleted, res, finalRes
#  f = open("in2.txt", 'r')
  f = open("D-small-attempt2.in", 'r')
  T = int(f.readline())
  for i in range(T):
    l = f.readline()
    [K, N] = [int(k) for k in l.split()]
    l = f.readline()
    keys = [0]*200
    require = [0]*200
    existing = [0]*200
    t = [0]*N
    deleted = [False]*N
    res = []
    trea = [[]]*N
    for k in l.split():
      ik = int(k)-1
      keys[ik] += 1
      existing[ik] += 1
    for j in range(N):
      trea[j] = [0]*200
      l = f.readline()
      ll = [int(k) for k in l.split()]
      t[j] = ll[0]-1
      require[ll[0]-1] += 1
      if ll[1] is not 0:
        for k in ll[2:]:
          trea[j][k-1]+=1
          existing[k-1]+=1
    res = decide(t,trea,K,N)
    if len(res) is not 0:
      result = [ str(k+1) for k in res]
      stdout.write("Case #%i: " % (i+1))
      stdout.write(' '.join(result))
      stdout.write('\n')
    else:
      stdout.write("Case #%i: " % (i+1))
      stdout.write("IMPOSSIBLE")
      stdout.write('\n')
    
solve()
