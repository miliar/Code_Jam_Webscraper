def pancakes(S, k, f, acc):
  acc.append(S)
  listS = list(S)
  flips = f
  min_flips = "IMPOSSIBLE"

  if check_pancake(S):
    return 0

  for i in range(len(S)):
    if S[i] == '-':
      
      for j in range(k):
        flip_t = flip_pancake(i - j, k, S)

        if check_pancake(flip_t):
          return flips + 1

        if flip_t not in acc:
          flip_t_flips = pancakes(flip_t, k, flips+1, acc)

          if flip_t_flips != "IMPOSSIBLE":
            if min_flips == "IMPOSSIBLE":
              min_flips = flip_t_flips
            elif flip_t_flips <= min_flips:
              min_flips = flip_t_flips

  return min_flips

def check_pancake(S):
  for c in S:
    if c != '+':
      return False
    
  return True

def flip_pancake(start, k, S):
  if start < 0:
    return S

  if start + k > len(S):
    return S

  listS = list(S)
  for i in range(k):
    if listS[start+i] == '-':
      listS[start+i] = '+'
    else:
      listS[start+i] = '-'

  return "".join(listS)

#main program
test_cases = int(raw_input())

for i in range(test_cases):
  test = raw_input()
  test_list = test.split()
  S = test_list[0]
  k = int(test_list[1])

  t_result = pancakes(S, k, 0, [])

  print "Case #{0}: {1}".format(i + 1, t_result)