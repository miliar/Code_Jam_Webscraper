
def get_result(D, locs):
  arrive = 0
  for k, s in locs:
    tmp = float(D - k) / s
    arrive = max(tmp, arrive)
  return D / arrive


num_tests = int(input())
for test_id in range(1, num_tests + 1):
  D, N = map(int, input().strip().split())
  locs = []
  for n in range(N):
    tmp = list(map(int, input().strip().split()))
    locs.append(tmp)
  res = get_result(D, locs)
  print("Case #{0}: {1}".format(test_id, res))

