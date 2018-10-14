def solve(N, K):
  states = [0 for i in range(N)]
  initial = states[:]
  power = 1
  K = K % (2**N)
  if (K + 1) == 2**N:
    return "ON"
  else:
    return "OFF"
  for it in range(K):
    # print "%s -> %d is online" % (str(states), power)
    for i in range(power):
      states[i] = 1 - states[i]
    power = 1
    cycle_len = -1
    while power < N and states[power - 1] == 1:
      power += 1
  # print "Final power is " + str(power)
  # print "Final states: " + str(states)
  if power == N and states[N-1] == 1:
    return "ON"
  else:
    return "OFF"
  
input = open("input.txt", "r").readlines()
output  = open("output.txt", "w")

NTest = int(input[0])
for it in range(NTest):
  parts = input[it + 1].split(" ")
  res = solve(int(parts[0]), int(parts[1]))
  output.write("Case #%d: %s\n" % (it + 1, res))

output.close()
  

