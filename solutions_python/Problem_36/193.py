#!/usr/bin/python

import sys
import string
import logging
import time

# logging.basicConfig(level=logging.INFO)

WELCOME = "welcome to code jam"

def count(goal, supply, mod=0):
  # In this puzzle, "x" is not a substring of "x" so,
  # we special case that.
  if goal == supply:
    return 0
  assert len(goal), "Only interested in non-trivial goals"
  logging.info("%s in %s" % (repr(goal), repr(supply)))
  return count_internal(goal, supply, cache={}, mod=mod)

def indexes(substr, fullstr):
  cur_index = -1
  while True:
    cur_index = fullstr.find(substr, cur_index + 1)
    if cur_index == -1:
      return
    else:
      yield cur_index

# We cache previous results of a stripped down version
# of our calculation.  The fancy term for this is 
# "dynamic programming".
def count_internal(goal, supply, cache, mod=0):
  if goal == "":
    return 1
  let, rest = goal[0], goal[1:]
  # Strip down to first occurrence of let
  i = supply.find(let)
  if i == -1:
    return 0
  supply = supply[i:]

  # If we've cached the value, use that.
  cached_value = cache.get((goal, supply))
  if cached_value is not None:
    return cached_value

  # Let's count 'em up!
  count = 0
  for i in indexes(let, supply):
    count += count_internal(rest, supply[i+1:], cache, mod = 0)
  if mod:
    count = (count % mod)
  cache[(goal, supply)] = count
  logging.info("%s in %s: %d" % (goal, supply, count))

  return count
    
def test(f):
  # Check indexes generator
  assert [1,3,8] == list(indexes("a", "0a2a4567a9"))
  # a is for assert
  def a(expected, goal, supply):
    for mod in [0, 1000]:
      start = time.time()
      actual = f(goal, supply, mod=mod)
      elapsed = time.time() - start
      if mod:
        expected = expected % mod
      if actual != expected:
        print "%s in %s.  Bad! Expected: %d.  Got: %d" % (goal, supply, expected, actual)
      else:
        print "%s in %s.  Good! %f seconds" % (goal, supply, elapsed)
  
  a(2*3*2*(3+1)*2, WELCOME, "wwelccmcomee t o coded e jamm")
  a(3*3*3*2, WELCOME, "wewelcomemte tooo code jjam")
  a(0, "a", "a")
  a(2, "a", "aa")
  a(3, "aa", "aaa")
  a(4, "ab", "aabb")
  a(8, "abc", "aabbcc")
  a(5+4+3, "ab", "abababbb")
  a(0, "foo", "foo")
  a(3 + 2 + 1 + 2 + 1 + 1, "abc", "abcabcabc")
  a(35, "www", "wwwwwww") # 7 choose 3

  # Now let's do some nasty ones
  s = """So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."""
  a(400263727, WELCOME, s)

  # 500 choose 30.
  a(1445259588120573502872111127079547366704414552400, 
    "x"*30, "x"*500)

  s = ""
  for x in WELCOME:
    s += x*40
  a(pow(40, len(WELCOME)), WELCOME, s)



def stupid_main(goal, supply):
  if goal == supply:
    return 0
  else:
    return stupid_count(goal, supply)

def stupid_count(goal, supply):
  if goal == "":
    return 1
  count = 0
  x = goal[0]
  rest = goal[1:]
  for i in indexes(x, supply):
    count += stupid_count(rest, supply[i+1:])
  return count

def enumerate_count(goal, supply, sofar=None, solutions=None, offset=0):
  if goal == "":
    solutions.append(tuple(sofar))
    return
  x = goal[0]
  rest = goal[1:]
  for i in indexes(x, supply):
    sofar.append(offset + i)
    enumerate_count(rest, supply[i+1:], sofar, solutions, 1 + offset + i)
    sofar.pop()

def enum_count(goal, supply, mod=0):
  logging.info(supply)
  if goal == supply:
    return 0
  sols = []
  enumerate_count(goal, supply, [], sols)
  s = set(sols)
  assert len(sols) == len(s)
  logging.info(sols)

  for s in sols:
    assert goal == "".join(supply[i] for i in s)
    assert sorted(s) == list(s), s

  return len(sols)

def dfa_count(goal, supply, mod=0):
  """
  We can make an NDFA and see how many times we get to go.
  Keeping state is hard, but all we care about is how many
  times we've gotten along a string.

  So state is an array of len(goal)+1 states, where we start
  at the 0th state.  Every time we get a match, we increment
  the number of people in state n+1 by the number of people in state.
  """
  if goal == supply:
    return 0

  counts = [ 0 for i in range(len(goal) + 1) ]
  counts[0] = 1
  index = {}
  for i, x in enumerate(goal):
    index.setdefault(x, []).append(i)
  # go from right to left in the update, so that we don't 
  # dirty stuff up
  for x in index.values():
    x.reverse()

  logging.info("\t".join("-" + goal))

  logging.info("\t".join(map(str, counts)))
  for x in supply:
    for i in index.get(x, []):
      counts[i+1] += counts[i]
    logging.info("\t".join(map(str, counts) + [x]))


  cnt = counts[len(goal)]
  if mod:
    cnt = (cnt % mod)
    
  return cnt
    
if __name__ == "__main__":
  f = dfa_count
  if False:
    test(f)
  else:
    input = file(sys.argv[1])
    num_problems = int(input.readline().strip())
    for i in range(num_problems):
      supply = input.readline().strip()
      print "Case #%d: %04d" % (i+1, f(WELCOME, supply) % 10000)
      # print "Case #%d: %04d" % (i+1, stupid_main(WELCOME, supply) % 10000)
