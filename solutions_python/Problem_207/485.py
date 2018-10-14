import itertools

def stableSolution(N, R, O, Y, G, B, V):
  if (G == R and N == G + R) or (O == B and N == O + B) or (V == Y and N == V + Y):
    return ''.join(['GR' for _ in xrange(G)] + ['OB' for _ in xrange(O)] + ['VY' for _ in xrange(V)])

  if (G > 0 and G + 1 > R) or (O > 0 and O + 1 > B) or (V > 0 and V + 1 > Y):
    return 'IMPOSSIBLE'

  remainingCounts = {}
  remainingCounts['R'] = R - ((G + 1) if G > 0 else 0)
  remainingCounts['B'] = B - ((O + 1) if O > 0 else 0)
  remainingCounts['Y'] = Y - ((V + 1) if V > 0 else 0)

  Gresult = ('R' + ''.join(['GR' for _ in xrange(G)]) if G > 0 else '')
  Oresult = ('B' + ''.join(['OB' for _ in xrange(O)]) if O > 0 else '')
  Vresult = ('Y' + ''.join(['VY' for _ in xrange(V)]) if V > 0 else '')

  if remainingCounts['R'] + remainingCounts['Y'] + remainingCounts['B'] == 0:
    result = Gresult + Oresult + Vresult
    if result[0] == result[-1]:
      return 'IMPOSSIBLE'
    return result

  complementaryCounts = {}
  complementaryCounts['R'] = G
  complementaryCounts['B'] = O
  complementaryCounts['Y'] = V

  result = ''
  sortedPrimaries = sorted(map(lambda color : (remainingCounts[color], -complementaryCounts[color], color), 'RBY'))[::-1]
  [(n1, _, c1), (n2, _, c2), (n3, _, c3)] = sortedPrimaries
  if n1 > n2 + n3 + 2:
    return 'IMPOSSIBLE'
  print n1, n2, n3
  extraColor = c1
  extraAmount = max(n1 - (n2 + n3), 0)
  if extraAmount > 0:
    n1 -= extraAmount
  # n2 pairs of 12, followed by (n1 - n2) pairs of the 13, with remaining (n3 + n2 - n1) inserted in 12 pairs
  print n1, n2, n3
  for _ in xrange(n3 + n2 - n1):
    result += ''.join([c1, c3, c2])
    for c in [c1, c2, c3]:
      remainingCounts[c] -= 1
  for _ in xrange(n1 - n3):
    result += ''.join([c1, c2])
    for c in [c1, c2]:
      remainingCounts[c] -= 1
  for _ in xrange(n1 - n2):
    result += ''.join([c1, c3])
    for c in [c1, c3]:
      remainingCounts[c] -= 1

  for permutation in itertools.permutations([extraColor for _ in xrange(extraAmount)] + filter(lambda x: len(x) > 0, [Oresult, Vresult, Gresult])):
    possibleString = [result] + list(permutation)
    L = len(possibleString)
    works = True
    for i in xrange(L):
      if possibleString[i % L][-1] == possibleString[(i + 1) % L][0]:
        works = False
        break
    if works:
      return ''.join(possibleString)

  if len(result) >= 3 and len(set(result[:3])) == 3:
    a = result[0]
    b = result[1]
    result = b + a + result[2:]
    for permutation in itertools.permutation([extraColor for _ in xrange(extraAmount)] + filter(lambda x: len(x) > 0, [Oresult, Vresult, Gresult])):
      possibleString = [result] + permutation
      L = len(possibleString)
      works = True
      for i in xrange(L):
        if possibleString[i % L][-1] == possibleString[(i + 1) % L][0]:
          works = False
          break
      if works:
        return ''.join(possibleString)

  return 'IMPOSSIBLE'

with open('../inputs/B-small-attempt0.in') as infile:
  with open('../outputs/B-small-attempt0.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [N, R, O, Y, G, B, V] = map(int, infile.readline().split(' '))
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(stableSolution(N, R, O, Y, G, B, V))
      outfile.write('\n')
