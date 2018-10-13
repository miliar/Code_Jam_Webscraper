from sys import maxint
import cPickle

INPUT = 'C-small.in'
OUTPUT = 'C-small.out'

def memoize(f):
  """
  Memoize function, clear cache on last return.
  """
  count = [0]
  cache = {}
  def g(*args, **kwargs):
    count[0] += 1
    try:
      try:
        if len(kwargs) != 0: raise ValueError
        hash(args)
        key = (args,)
      except:
        key = cPickle.dumps((args, kwargs))
      if key not in cache:
        cache[key] = f(*args, **kwargs)
      return cache[key]
    finally:
      count[0] -= 1
      if count[0] == 0:
        cache.clear()
  return g


def release(cells, c):

    cost = 0
    if c <= len(cells):
        for i in range(c, len(cells)):
            if cells[i]:
                cost += 1
            else:
                break
        for i in range(c-2,-1,-1):
            if cells[i]:
                cost += 1
            else:
                break
    return cost
        
                       

def backtrack(cells, released, coins):
    min = maxint
    if not released:
        return coins
    else:
        for c in released:
            cost = release(cells, c)
            coins += cost
            cells[c-1] = False
            newReleased = released[:]
            newReleased.remove(c)
            newCost = backtrack(cells, newReleased, coins)
            if newCost < min:
                min = newCost
            cells[c-1] = True
            coins -= cost
    return min

backtrack = memoize(backtrack)            

if __name__=='__main__':

    input = open(INPUT)
    output = open(OUTPUT, 'w')
    N = int(input.readline().strip())
    for i in range(N):
        P,Q = [int(j) for j in input.readline().strip().split()]
        released = [int(j) for j in input.readline().strip().split()]
        cells = [True]*P
        coins = backtrack(cells,released,0)
        output.write('Case #%d: %d\n' % (i+1, coins))
        #print 'Case #%d: %d' % (i+1, coins)
    output.close()

#print backtrack([True,True],[1,2],0)
