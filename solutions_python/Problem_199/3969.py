def count_flips(S, K, flips=0):
    pluses, minus, remainder = S.partition("-")
    if pluses == S:
        return flips
    if len(remainder) < K-1:
        return 'IMPOSSIBLE'
    else:
        rest = '+'
        for i in range(0, K-1):
            if remainder[i] == '-' : rest += '+'
            else: rest += '-'
        rest += remainder[K-1:]
        flips += 1
        return count_flips(rest, K, flips)


t = int(input())
for i in range(1, t + 1):
  S, K = [c for c in input().split(" ")]
  K = int(K)
  print("Case #{}: {}".format(i, count_flips(S,K)))