# 4:54 start
T = int(input())
for i in range(1, T + 1):
  N, K = map(int, input().split(" "))
  space = [N]
  for j in range(K-1):
    x = max(space)
    space.remove(x)
    space.append(x//2)
    space.append(x-1-x//2)
    # print(space)
  x = max(space)
  print("Case #{}: {} {}".format(i, x//2, x-x//2-1))
