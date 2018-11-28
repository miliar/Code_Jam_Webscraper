
def solve(k, s):
    count = 0
    flips = [False for _ in range(0,k)]
    for i in range(0, len(s) - k + 1):
        if (s[i] == '+') != flips[0]:
            flips = flips[1:]
        else:
            count += 1
            flips = [not x for x in flips[1:]]
        flips.extend([False])

    for i in range(1, k):
        if (s[len(s)-k+i] == '+') == flips[i-1]:
            return -1

    return count

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = [s for s in input().split(" ")]
  res = solve(int(k), s)

  if res == -1:
      print("Case #{}: IMPOSSIBLE".format(i))
  else:
      print("Case #{}: {}".format(i, res))
  # check out .format's specification for more formatting options
