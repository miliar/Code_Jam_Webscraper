t = int(raw_input())

for i in range(t):
  f_a = []
  s_a = []

  a = int(raw_input())

  for j in range(4):
    s = raw_input()
    s = s.split()

    f_a.append(s)
  
  b = int(raw_input())

  for j in range(4):
    s = raw_input()
    s = s.split()

    s_a.append(s)

  poss_ans_1 = f_a[a-1]

  poss_ans_2 = []

  for j in poss_ans_1:
    if j in s_a[b-1]:
      poss_ans_2.append(j)

  x = len(poss_ans_2)

  if x == 0:
    print "Case #%d: Volunteer cheated!"%(i+1)
  elif x > 1:
    print "Case #%d: Bad magician!"%(i+1)
  else:
    print "Case #%d: %s"%(i+1, poss_ans_2[0])
   

