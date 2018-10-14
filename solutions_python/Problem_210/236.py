def main():
  for t in xrange(int(raw_input())):
    (C, J) = (int(x) for x in raw_input().split())
    cTimes = []
    jTimes = []
    for c in xrange(C):
      (s, e) = (int(x) for x in raw_input().split())
      cTimes.append((s,e))
    for j in xrange(J):
      (s, e) = (int(x) for x in raw_input().split())
      jTimes.append((s,e))
    cTimes.sort()
    jTimes.sort()
    allTimes = cTimes + jTimes
    allTimes.sort()
    if allTimes == cTimes + jTimes or jTimes + cTimes:
      if len(cTimes) > 1 and cTimes[1][1] - cTimes[0][0] > 720 and cTimes[0][1] + 1440 - cTimes[1][0] > 720:
        ans = 4
      elif len(jTimes) > 1 and jTimes[1][1] - jTimes[0][0] > 720 and jTimes[0][1] + 1440 - jTimes[1][0] > 720:
        ans = 4
      else:
        ans = 2
    else:
      ans = 4
    print "Case #{}: {}".format(t+1, ans)

if __name__ == "__main__":
  main()
