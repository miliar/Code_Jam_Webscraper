_T = int(raw_input())
for _t in range(1, _T+1):
  N, P = map(int, raw_input().split())
  G = map(int, raw_input().split())
  M = [0]*P

  for g in G:
    M[g%P] += 1

  res = M[0]

  if P == 2:
    res += (M[1] + 1)/2
  elif P == 3:
    tmp = min(M[1], M[2])
    res += tmp
    M[1] -= tmp
    M[2] -= tmp

    tmp = max(M[1], M[2])
    res += (tmp + 2)/3
  else:
    tmp = min(M[1], M[3])
    res += tmp
    M[1] -= tmp
    M[3] -= tmp
    res += M[2]/2
    M[2] -= (M[2]/2)*2

    tmp = max(M[1], M[3])
    if M[2] == 0:
      res += (tmp + 3)/4
    else:
      res += (tmp + 5)/4


  
  print 'Case #{}: {}'.format(_t, res)
