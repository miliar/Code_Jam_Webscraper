# python3
T = int(input())
for t in range(1, T + 1):
  B = [0 for _ in range(17)]
  for a in range(2):
    r = int(input())
    m = [list(map(int, input().split())) for _ in range(4)]
    for c in m[r-1]:
      B[c] += 1
  two, who = 0, -1
  for idx, b in enumerate(B):
    if b == 2:
      two += 1
      who = idx
  if two > 1:
    print("Case #{}: Bad magician!".format(t))
  elif two == 1:
    print("Case #{}: {}".format(t, who))
  else:
    print("Case #{}: Volunteer cheated!".format(t))

