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
    lines = map(str.rstrip, f.readlines())
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        print "Case #%d:" % (testcase),

        totaldata = []
        o_data = []
        b_data = []
        moveto = []
        totaldata = lines.pop(0).split(' ')
        N = int(totaldata.pop(0))
        i = 0
        time = 0
        present_position = {
            'O': 1,
            'B': 1,
        }
        next = {'O': [], 'B': []}
        fulldata = []
        def other(bot):
            if bot == 'O':
                return 'B'
            else:
                return 'O'

        while len(totaldata):
            bot = totaldata.pop(0)
            pos = totaldata.pop(0)
            fulldata.append((bot, pos))
            next[bot].append(int(pos))

        def adjustpos(bot, time):
##             print "%d - %d" % (next[bot][0], present_position[bot])
            position = -1
            if (len(next[bot]) == 0):
                return present_position[bot]
##             print "here for %s: from %s to %s (in %s)" % (bot, present_position, next[bot][0], time)
            if (next[bot][0] > present_position[bot]):
                if present_position[bot] + time >= next[bot][0]:
                    position = next[bot][0]
                else:
                    position = present_position[bot] + time
            elif (next[bot][0] < present_position[bot]):
                if present_position[bot] - time <= next[bot][0]:
                    position = next[bot][0]
                else:
                    position = present_position[bot] - time
            else:
                position = next[bot][0]
##             print "returning %d" % position
            return position
        totaltime = 0
        while len(fulldata):
##             print "ENTRY: %s - %s - %s" % (present_position, next, fulldata)
            bot, nextpos = fulldata.pop(0)
            nextpos = int(nextpos)
            time = abs(nextpos - present_position[bot]) + 1
            totaltime += time
            present_position[bot] = nextpos
            present_position[other(bot)] = adjustpos(other(bot), time)
            next[bot].pop(0)
##             print "EXIT: %s - %s - %s [TIME: %d]" % (present_position, next, fulldata, time)
        print totaltime
        testcase += 1

if __name__ == '__main__':
    main()
