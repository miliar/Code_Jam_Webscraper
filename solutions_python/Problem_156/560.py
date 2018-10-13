
def solve_case_wrong(P):
  results = []
  for i in range(max(P) + 10):
    P.sort()
    results.append(P[-1] + i)
    lrg_e = max(P)
    largest_element = P.pop()
    split_1 = largest_element / 2
    split_2 = largest_element / 2
    if largest_element % 2 == 1:
      split_2 += 1
    P.append(split_1)
    P.append(split_2)
  return min(results)

def get_num_divisions(height, target_height):
  assert target_height > 0
  result = height / target_height - 1
  if height % target_height != 0:
    result += 1
  return result

def solve_case(P):
  results = []
  P.sort()
  for target_height in range(1, P[-1] + 1):
    num_divisions = 0
    for i in range(len(P) - 1, -1, -1):
      if P[i] > target_height:
        num_divisions += get_num_divisions(P[i], target_height)
      else:
        break
    results.append(target_height + num_divisions)
  return min(results)

with open('B-large.in', 'r') as f:
  num_cases = int(f.readline())
  for case_num in range(num_cases):
    num = f.readline()
    P = [int(x) for x in f.readline().split()]
    print 'Case #{0}:'.format(case_num + 1), solve_case(list(P))
