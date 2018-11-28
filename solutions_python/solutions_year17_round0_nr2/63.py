def dstr(i):
  i = int(i) - 1
  return str(i) if i else ""

def last_tidy(sn):
  last_inc = 1
  for i in range(1, len(sn)):
    if sn[i-1] < sn[i]:
      last_inc = i + 1
    if sn[i-1] > sn[i]:
      return dstr(sn[:last_inc]) + "9" * (len(sn) - last_inc)
  return sn

T = int(input())
for t in range(T):
  print("Case #{}: {}".format(t+1, last_tidy(input())))
