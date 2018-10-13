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

def flip(array, index):
    array[index] = str(int(array[index]) - 1)
    i = 1
    while index + i < len(array):
        array[index+i] = '9'
        i += 1
    return array

def get_largest_tidy(array):
    if len(array) == 1:
        return "".join(array)
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return get_largest_tidy(flip(array, i))
    return "".join(array).lstrip("0")

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        line = (lines.pop(0)).rstrip()
        number = list(line)
        largest_tidy = get_largest_tidy(number)
        print "Case #{}: {}".format(testcase, largest_tidy)
        testcase += 1

if __name__ == '__main__':
    main()
