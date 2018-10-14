def do_flip(pancakes, pos, pan_width):
  return pancakes[:pos] \
      + ''.join([ '+' if pancakes[i] == '-' else '-' for i in range(pos,pos+pan_width)]) \
      + pancakes[pos+pan_width:]

def naive(pancakes, pan_width, flips = 0):
  """
    Find first unhappy pancake at index i, flip pancakes [i,i+k]
    Pancake i is now happy
    Repeat until either:
      - all pancakes are happy (HAPPY CASE), or
      - i+k > len(str_pancakes) (IMPOSSIBLE)
  """
  while (True):
    pos = pancakes.find("-")
    if pos == -1:
      return flips
    elif pos > (len(pancakes) - pan_width):
      # flipping rightmost k pancakes would make sad some pancakes on the left!
      return None
    else:
      flips += 1
      pancakes = do_flip(pancakes, pos, pan_width)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def main(fnStrategy):
  t = int(raw_input())  # read a line with a single integer
  for i in xrange(1, t + 1):
    pancakes, pan_width = raw_input().split(" ")
    res = fnStrategy(pancakes, int(pan_width))
    print "Case #{}: {} ".format(i, res if res is not None else "IMPOSSIBLE")

main(naive)

