import sys
rl = lambda : sys.stdin.readline()

def rotations(num, a, b):
  rotations = []
  rot = str(num)
  for i in range(-1, len(rot) * -1, -1):
    rotations.append(rot[i:] + rot[:i])
  
  rotations = [rot for rot in rotations if int(rot) >= a and int(rot) <= b]
  rotations = [rot for rot in rotations if rot != str(num)]
  rotations = [rot for rot in rotations if rot[0] != '0']
  rotations = [rot for rot in rotations if num < int(rot)]
  return rotations

def solve(case):
  pair = []
  count = 0
  a,b = rl().strip().split(' ')
  a,b = int(a), int(b)
  for i in range(a, b + 1, 1):
    result = rotations(i, a, b)
    for res in result:
      pair.append((i, res))
    count += len(set(result))

  #print(pair)
  print('Case #' + str(case) + ': ' + str(count))
  #print(set(pair))
  #print(len(set(pair)))


num_cases = int(rl())

for case in range(1, num_cases + 1, 1):
  solve(case)
