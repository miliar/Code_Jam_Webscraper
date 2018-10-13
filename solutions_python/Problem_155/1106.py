cases = input()
for case in range(cases):
    smax, ss = raw_input().split(" ")
    smax = int(smax)
    ss = [int(x) for x in list(ss)]
    result = 0
    sum = 0
    for s, num in enumerate(ss):
      shortage = max(s - sum, 0)
      result += shortage
      sum += num + shortage
    print "Case #%d: %d" % (case + 1, result)
