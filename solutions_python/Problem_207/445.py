
def get_result(R, O, Y, G, B, V):
  assert O == 0
  assert G == 0
  assert V == 0
  max_cnt = max(R, Y, B)
  if Y + B < max_cnt or R + B < max_cnt or R + Y < max_cnt:
    return "IMPOSSIBLE"
  cnts = [(R, "R"), (B, "B"), (Y, "Y")]
  cnts = sorted(cnts, key=lambda x:x[0], reverse=True)

  s = [""] * (3 * max_cnt)
  for i in range(cnts[0][0]):
    s[3 * i] = cnts[0][1]
  for i in range(cnts[1][0]):
    s[3 * i + 1] = cnts[1][1]
  for i in range(cnts[2][0]):
    s[3 * max_cnt - 1 - 3 * i] = cnts[2][1]
  return "".join(s)

num_tests = int(input())
for test_id in range(1, num_tests + 1):
  N, R, O, Y, G, B, V = map(int, input().strip().split())
  res = get_result(R, O, Y, G, B, V)
  print("Case #{0}: {1}".format(test_id, res))


