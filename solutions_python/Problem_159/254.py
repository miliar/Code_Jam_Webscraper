debug = True

def pairwise_differences(lst):
  return [a-b for a, b in zip(lst, lst[1:])]

T = int(raw_input())
for case in range(T):
  N = int(raw_input())
  m = map(int, raw_input().split())

  differences = pairwise_differences(m)
  first_method = sum(max(difference, 0) for difference in differences)
  second_rate = max(differences)  # per 10 seconds
  second_method = sum(min(mi, second_rate) for mi in m[:-1])

  print "Case #{}: {} {}".format(case + 1, first_method, second_method)
