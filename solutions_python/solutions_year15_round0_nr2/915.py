def upper(i):
  if i%2 == 0:
    return i/2
  else:
    return (i+1)/2

def lower(i):
  if i%2 == 0:
    return i/2
  else:
    return (i-1)/2

def min_time(l):
  if l[0] <= 3:
    return l[0]

  t_unsplit = l[0]

  if len(l) >= 4 and l[3] == 9:
    return 9

  for j in range(2,l[0]-1):
    l_new = l[:]
    #l_new.append(upper(l[0]))
    l_new.append(l[0]-j)
    #l_new[0] = lower(l[0])
    l_new[0] = j
    l_new.sort(reverse=True)
    t_unsplit = min(t_unsplit, 1+min_time(l_new))
  #print(l_new)
  #t_split = 1+min_time(l_new)
  #return min(t_split, t_unsplit)
  return t_unsplit

for i in range(int(raw_input())):
  p = []
  d = int(raw_input())
  p = map(int, raw_input().split())
  p.sort(reverse=True)
  print("Case #%d: %d" % (i+1, min_time(p)))
