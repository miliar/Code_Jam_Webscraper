T = raw_input()
for t in range(int(T)):
  a1 = int(raw_input())
  r1 = []
  for i in range(4):
    r1.append(map(int, raw_input().split()))
  
  a2 = int(raw_input())
  r2 = []
  for i in range(4):
    r2.append(map(int, raw_input().split()))

  ans = []
  for i in r1[a1-1]:
    if i in r2[a2-1]:
      ans.append(i)
  if len(ans) == 1:
    ans = str(ans[0])
  elif len(ans) == 0:
    ans = 'Volunteer cheated!'
  elif len(ans) > 1:
    ans = 'Bad magician!'

  print 'Case #%d: %s' % (t+1, ans)
  

  
  