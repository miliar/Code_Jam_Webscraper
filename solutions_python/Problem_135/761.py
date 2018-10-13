def solve(fA,first,sA,second):
  f = set(first[fA])
  s = set(second[sA])

  inter = f.intersection(s)
  
  if len(inter) == 1 :
    return str(inter.pop())
  elif len(inter)==0:
    return 'Volunteer cheated!'
  elif len(inter)>1:
    return 'Bad magician!'

T = int(raw_input())

for i in xrange(T):
  fA = int(raw_input()) - 1
  first = []
  for _ in range(4):
    first.append(map(int,raw_input().split()))
  sA = int(raw_input()) - 1
  second = []
  for _ in range(4):
    second.append(map(int,raw_input().split()))
  sol = solve(fA,first,sA,second)
  print 'Case #' + str(i+1) + ': ' + str(sol)

