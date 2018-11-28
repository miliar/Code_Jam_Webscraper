
SOL = []
gs1 = 1000
gs2 = -1000

def check(L):
  global gs1, gs2
  s1 = SOL[0]
  i = 1
  while i < L: 
    s1 = s1*10 + SOL[i]
    i += 1
  s2 = SOL[L]
  i = L + 1
  while i < 2*L:
    s2 = s2*10 + SOL[i]
    i += 1

  #print L, SOL, s1, s2

  if abs(s1-s2) < abs(gs1 - gs2):
    gs1, gs2 = s1, s2
    return

  if abs(s1-s2) == abs(gs1 - gs2):
    if s1 < gs1:
      gs1, gs2 = s1, s2
      return
    if s1 == gs1 and s2 < gs2:
      gs1, gs2 = s1, s2
      return

def sol2(S, L, pos):
  if pos == L:
    check(L / 2)
    return
  if S[pos] != '?':
    SOL[pos] = int(S[pos])
    sol2(S, L, pos+1)
  else:
    for d in range(10):
      SOL[pos] = d
      sol2(S, L, pos+1)

def sol(S1, S2, mode):
  
  if not S1: return '', ''
  
  if mode == 0 and S1[0] == '?' and S2[0] == '?': 
    s1, s2 = sol(S1[1:], S2[1:], 0)
    return '0' + s1, '0' + s2
    
  if mode == 0 and S1[0] == '?' and S2[0] != '?':
    s1, s2 = sol(S1[1:], S2[1:], 0)
    return S2[0] + s1, S2[0] + s2
     
  if mode == 0 and S1[0] != '?' and S2[0] == '?':
    s1, s2 = sol(S1[1:], S2[1:], 0)
    return S1[0] + s1, S1[0] + s2

  if mode == 0 and S1[0] != '?' and S2[0] != '?':
    
    if S1[0] == S2[0]:
      s1, s2 = sol(S1[1:], S2[1:], 0)
      return S1[0] + s1, S2[0] + s2
    elif S1[0] < S2[0]:
      s1, s2 = sol(S1[1:], S2[1:], 1)
      return S1[0] + s1, S2[0] + s2
    else:
      s1, s2 = sol(S1[1:], S2[1:], -1)
      return S1[0] + s1, S2[0] + s2

  if mode == 1:
    s1, s2 = sol(S1[1:], S2[1:], 1)
    if S1[0] != '?': sc1 = S1[0]
    else:            sc1 = '9' 
    if S2[0] != '?': sc2 = S2[0]
    else:            sc2 = '0' 
    return sc1 + s1, sc2 + s2

  if mode == -1:
    s1, s2 = sol(S1[1:], S2[1:], -1)
    if S1[0] != '?': sc1 = S1[0]
    else:            sc1 = '0' 
    if S2[0] != '?': sc2 = S2[0]
    else:            sc2 = '9' 
    return sc1 + s1, sc2 + s2
    


def solve(N):
  global SOL, gs1, gs2
  part = N.split(' ')
  S1, S2 = part[0], part[1]
  #s1, s2 = sol(S1, S2, 0)
  SOL = [0 for i in range(len(S1 + S2))]
  sol2(S1 + S2, len(S1 + S2), 0)
  #if int(s1) != gs1 or int(s2) != gs2: print N, gs1, gs2, s1, s2
  #return s1 + ' ' + s2
  
  gs1 = str(gs1)
  gs2 = str(gs2)
  
  while len(gs1) < len(S1): gs1 = '0' + gs1
  while len(gs2) < len(S2): gs2 = '0' + gs2
  
  return gs1 + ' ' + gs2
  

f = open('B-small-attempt2.in')
fo = open('output_B_small_2.out', 'w')

#f = open('input_B.txt')
#fo = open('output_B.out', 'w')


NT = int(f.readline())
for t in xrange(NT):
  N = f.readline().strip()
  fo.write('Case #' + str(t+1) + ': ' + str(solve(N)) + '\n')
  gs1 = 1000
  gs2 = -1000

f.close()
fo.close()