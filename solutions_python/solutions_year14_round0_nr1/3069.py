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

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        row = int(lines.pop(0))
        row -= 1
        matrix1 = []
        for i in (1, 2, 3, 4):
            matrix1.append(lines.pop(0).rstrip().split(" "))
        poss1 = matrix1[row]
##         hash1 = dict(zip(poss1, [ 1 for x in poss1 ]))
##         print hash1
##         exit(0)

        row = int(lines.pop(0))
        row -= 1
        matrix2 = []
        for i in (0, 1, 2, 3):
            matrix2.append(lines.pop(0).rstrip().split(" "))
        poss2 = matrix2[row]
##         hash2 = dict(zip(poss2, [ 1 for x in poss2 ]))

        common = set(poss1) & set(poss2)
        result = ""
        if (len(common) == 1):
            result = list(common)[0]
        elif (len(common) == 0):
            result = "Volunteer cheated!"
        else:
            result = "Bad magician!"

        print "Case #%d: %s" % (testcase, result)
        testcase += 1

if __name__ == '__main__':
    main()
