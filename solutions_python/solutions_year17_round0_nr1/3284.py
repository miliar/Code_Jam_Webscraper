from collections import deque

def solve(input):
  state = [True if x == '+' else False for x in input.split(' ')[0]]
  size = int(input.split(' ')[1])

  q = deque()
  q.append((state, 0))
  tested = set()
  while True:
    if len(q) == 0:
      return 'IMPOSSIBLE'
    state, moves = q.popleft()
    if str(state) in tested:
      continue

    tested.add(str(state))
    if state == [True]*len(state):
      return moves
    for i in range(len(state)-size+1):
      nstate = list(state)
      for j in range(i, i+size):
        nstate[j] = not nstate[j]
      q.append((nstate, moves+1))

T = int(raw_input())
for i in range(T):
  print 'Case #' + str(i+1) + ': ' + str(solve(raw_input()))