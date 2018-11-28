DEBUG = True
DEBUG = False

def print_res(case, data):
  print("Case #{}: {}".format(case, data))

T = int(input())

for t in range(1, T + 1):
  S, K = input().split()
  S = list(S)
  K = int(K)
  seed = '-'
  counter = 0
  flipped_idxs = []
  fidx = None

  for si in range(0, len(S)):
    if S[si] == seed and si + K <= len(S):
      if fidx is None:
        fidx = si + K
      else:
        flipped_idxs.append(si + K)

      seed = '+' if seed == '-' else '-'
      counter += 1
    elif S[si] == seed and si + K >= len(S):
      counter = 'IMPOSSIBLE'
      break
    
    if fidx is not None and fidx == si + 1:
      seed = '+' if seed == '-' else '-'
      if len(flipped_idxs) > 0:
        fidx = flipped_idxs[0]
        flipped_idxs = flipped_idxs[1:]
      else:
        fidx = None

    if DEBUG:
      print(S)
      print("S[si]: {}, si: {}, seed: {}".format(S[si], si, seed))
      print(fidx, flipped_idxs)
      print("counter: {}".format(counter))


  print_res(t, counter)
