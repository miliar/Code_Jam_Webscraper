input = open("input.txt", "r").readlines()
output  = open("output.txt", "w")

def next(pos, K, groups):
  start_pos = pos
  N = len(groups)
  tot = groups[pos]
  while (pos + 1) % N != start_pos and tot + groups[(pos + 1) % N] <= K:
    pos = (pos + 1) % N
    tot += groups[pos]
  return start_pos, pos, tot
  
def solve(R, K, groups):
  N = len(groups)
  pos = 0
  profit = 0
  if R > 10000:
    for it in range(10000):
      indices = next(pos, K, groups)
      profit += indices[2]
      pos = (indices[1] + 1) % N
    R -= 10000

  starting_pos = pos
  starting_profit = profit
  profit_per_cycle = 0
  cycle_len = 0
  for it in range(10000):
    indices = next(pos, K, groups)
    profit += indices[2]
    pos = (indices[1] + 1) % N
    if pos == starting_pos:
      cycle_len = it + 1
      profit_per_cycle = profit - starting_profit
      break

  profit = starting_profit
  pos = starting_pos

  if cycle_len > 0 and R > 10000:
    R = R % cycle_len
    profit += profit_per_cycle * (R / cycle_len)

  for it in range(R):
    indices = next(pos, K, groups)
    profit += indices[2]
    pos = (indices[1] + 1) % N
  return profit

NTest = int(input[0])
for it in range(NTest):
  R, K, N = input[it * 2 + 1].split(" ")
  parts = input[2 * it + 2].split(" ")
  numbers = [int(x) for x in parts]
  assert int(N) == len(parts)
  res = solve(int(R), int(K), numbers)
  output.write("Case #%d: %d\n" % (it + 1, res))

output.close()
  

