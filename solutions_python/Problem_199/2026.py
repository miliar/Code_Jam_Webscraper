IMPOSSIBLE = 'IMPOSSIBLE'


def main():
  T = int(raw_input())
  for i in range(T):
      line = raw_input()
      S, K = line.split(' ')
      K = int(K)

      result = run_case(S, K)
      print 'Case #{}: {}'.format(i+1, result)


def run_case(s, k):
    if is_done(s):
        return 0

    flips = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            s = flip_at(s, k, i)
            flips += 1
        if is_done(s):
            return flips

    return IMPOSSIBLE


def flip_at(s, k, i):
    assert k > 0 and i >= 0
    assert (i + k) <= len(s)
    flipper = {'-': '+', '+': '-'}
    return '{}{}{}'.format(
        s[:i], ''.join(flipper[c] for c in s[i:i+k]), s[i+k:])


def is_done(s):
    return all(c is '+' for c in s)


if __name__ == '__main__':
  main()
