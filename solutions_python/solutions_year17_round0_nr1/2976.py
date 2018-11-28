flip_map = {}

def gen_flip_map(pancake_count, at_a_time):
  fmap = [[] for i in range(pancake_count)]
  flip_type= pancake_count - at_a_time + 1;
  for i in range(flip_type):
    for j in range(at_a_time):
      fmap[i+j].append(i)
  return fmap;

def solve(pancakes, at_a_time):
  # map generation
  pc = len(pancakes)
  if (pc, at_a_time) in flip_map:
    fmap = flip_map[(pc, at_a_time)]
  else:
    fmap = gen_flip_map(pc, at_a_time)
    flip_map[(pc, at_a_time)] = fmap

  # solve phase
  flip_type = pc - at_a_time + 1;
  # 1 for even, -1 for odd
  parity = [0 for i in range(flip_type)]
  for i in range(flip_type):
    p = 1
    types = fmap[i]
    for t in types:
      p *= parity[t] if parity[t] != 0 else pancakes[t]
    parity[i] = p

  # verification phase
  for i in range(flip_type, pc):
    p = 1
    types = fmap[i]
    for t in types:
      p *= parity[t]
    if pancakes[i] * p != 1:
      return -1

  # verification passed, compute number of flips
  num_flip = 0
  for p in parity:
    if p == -1:
      num_flip += 1

  return num_flip

def test():
  pancakes, at_a_time = input().split(' ')
  pancakes = [1 if p == '+' else -1 for p in pancakes]
  at_a_time = int(at_a_time)
  print(solve(pancakes, at_a_time))

def main():
  T = int(input())
  for i in range(T):
    pancakes, at_a_time = input().split(' ')
    pancakes = [1 if p == '+' else -1 for p in pancakes]
    at_a_time = int(at_a_time)
    ans = solve(pancakes, at_a_time)
    print('Case #%d: %s' % (
      i+1,
      str(ans) if ans >= 0 else 'IMPOSSIBLE'
    ))

# test()
main()
