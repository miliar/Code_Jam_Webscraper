def main():
  L, D, N = map(int, raw_input().split())
  S = []
  for i in range(D):
    S.append(raw_input())
  for i in range(N):
    print 'Case #%d:' % (i+1),
    pattern = raw_input()
    ok = [True] * D
    idx = 0
    while len(pattern) > 0:
      if pattern[0] == '(':
        next = pattern.index(')')
        close = pattern[1:next]
        pattern = pattern[next+1:]
        for i, s in enumerate(S):
          if s[idx] not in close:
            ok[i] = False
      else:
        for i, s in enumerate(S):
          if s[idx] != pattern[0]:
            ok[i] = False
        pattern = pattern[1:]
      idx += 1
    print sum(ok)


if __name__ == '__main__':
  main()
