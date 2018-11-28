#! /usr/bin/python
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func

## @tail_call_optimized

def uniq(list):
    seen = {}
    for x in list:
        seen[x] = 1 
    return seen.keys()

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        print "Case #%d:" % (testcase),
        N = lines.pop(0).strip()
        c = map(int, lines.pop(0).split())
        from operator import xor
        if reduce(xor, c):
            print "NO"
        else:
            print sum(c) - min(c)
        testcase += 1

if __name__ == '__main__':
    main()

