#! /usr/bin/python
import sys
import pprint
PP = pprint.PrettyPrinter(indent=4).pprint

def tail_call_optimized(g):
  def function(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise Exception(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except Exception as e:
          args = e.args
          kwargs = e.kwargs
  return function

def flip(state, k, start):
    flipped = {
        "+": "-",
        "-": "+",
    }
    for i in range(k):
        state[start+i] = flipped[state[start+i]]
    return

@tail_call_optimized
def can_flip(state, k):
    count = 0
    for i in range(len(state)):
        if i >= len(state)-k+1:
            if all(x == "+" for x in state[i:]):
                return count
            else:
                return "IMPOSSIBLE"
        if state[i] == "+":
            continue
        flip(state, k, i)
        count += 1
            # if 
    
    print "here with count {}".format(count)
    return

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        line = (lines.pop(0)).rstrip()
        (pancake_state, k_size) = line.split(" ")
        pancake_state = list(pancake_state)
        K = int(k_size)
        count = can_flip(pancake_state, K)
        print "Case #{}: {}".format(testcase, count)
        testcase += 1

if __name__ == '__main__':
    main()
