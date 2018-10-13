
def build_permutations(n, m):
  result = list()
  if n == 0:
    return result
  if n == 1:
    return [[1]]
  for i in range(1, min(n + 1, m + 1)):
    if i < n:
      lol = build_permutations(n - i, min(i, m))
      for l in lol:
        newlist = [i]
        newlist.extend(l)
        result.append(newlist)
    else:
      newlist = [i]
      result.append(newlist)
  return result


def possible_splits(n):
  return build_permutations(n, n)


def split_stack(n, splits):
  k = splits + 1
  if n % k == 0:
    return [n // k] * k
  else:
    l1 = [(n // k) + 1] * (n % k)
    l2 = [n // k] * (k - (n % k))
    return l1 + l2

def max_split(n, splits):
  k = splits + 1
  if n % k == 0:
    return n // k
  else:
    return (n // k) + 1

def do_split(cakes, split, best):
  lc = len(cakes)
  ls = len(split)
  if ls > lc: return 0
  worst = 0
  if lc > ls:
    worst = max(worst, cakes[ls])
  for i in range(0, ls):
    if worst > best: return 0
    if split[i] >= cakes[i]: return 0
    worst = max(worst, max_split(cakes[i], split[i]))
  return worst


with open('input.txt') as fin:
  with open('output.txt', mode='w') as fout:
    T = int(fin.readline())
    for t in range(1, T + 1):
      D = int(fin.readline())
      cakes = [int(x) for x in fin.readline().split()]
      cakes.sort(reverse=True)
      best = cakes[0]
      maxsplits = best - 1

      for numsplits in range(1, maxsplits):
        print("case {}: {} splits, best = {}".format(t, numsplits, best))
        if numsplits >= best:
          break
        poss = possible_splits(numsplits)
        for spl in poss:
          newbest = do_split(cakes, spl, best)
          if newbest > 0:
            best = min(best, newbest + numsplits)

      fout.write("Case #{}: {}\n".format(t, best))

