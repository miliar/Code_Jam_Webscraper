
n = int(raw_input())
for c in range(n):
  (A,B) = (int(r) for r in raw_input().split(' '))
  L = len(str(B))
  ans = []
  out = 0
  # The odd ones out
  for v in (1,4,9):
    if A <= v <= B:
      ans.append(v)
      out += 1
  # Twos
  for d in range(L/2+2):
    s = '2'+'0'*d+'2'
    sq = int(s)**2
    #print s,sq
    if A <= sq <= B: out += 1 
    if A <= sq <= B: ans.append(sq)
  for d in range(L/4+2):
    s = '2'+'0'*d+'1'+'0'*d+'2'
    sq = int(s)**2
    if A <= sq <= B: out += 1
    if A <= sq <= B: ans.append(sq)
  # Binary
  p = [0,0,0,0,0]
  beg = set()
  for p[0] in range(L/4+2):
   for p[1] in range(min(p[0],L/4+1),L/4+2):
    for p[2] in range(min(p[1],L/4+1),L/4+2):
     for p[3] in range(min(p[2],L/4+1),L/4+2):
      for p[4] in range(min(p[3],L/4+1),L/4+2):
        s = ['0'] * (L/4+1)
        for pos in range(5):
          if p[pos] < (L/4+1): s[p[pos]] = '1'
        a = ''.join(s)
        a = a[(a+'1').find('1'):]
        beg.add(a)
  for b in beg:
   if b:
    if sum([int(u) for u in b]) >= 5: continue
    rev = [b+b[::-1],b+'0'+b[::-1],b+'1'+b[::-1],b+'2'+b[::-1]]
    for v in rev:
      v2 = int(v)**2
      s = str(v2)
      if A <= v2 <= B and s == s[::-1]: out += 1
      if A <= v2 <= B and s == s[::-1]: ans.append(v2)
  print "Case #%d: %d" % (c+1,out)
  #y = len(list(set(range(A,B+1)).intersection(set([1,4,9,121,484]))))
  #print A,B, ans

