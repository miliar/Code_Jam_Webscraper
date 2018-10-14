ntc = input()
for itc in range(ntc):
  n = input()
  naomi = map(float, raw_input().split())
  ken = map(float, raw_input().split())
  for arr in [naomi, ken]:
    for i in range(n):
      arr[i] = int(arr[i] * 100000)

  def Calc(ar1, ar2):
    ar2low = sorted(ar2)
    ar2low = ar2low[::-1]
    ret = 0
    for i in sorted(ar1):
      if i > ar2low[-1]:
        ret += 1
        ar2low.pop()
    return ret
  print 'Case #{0}: {1} {2}'.format(itc+1, Calc(naomi, ken), n- Calc(ken, naomi))


