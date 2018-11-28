import sys

def thing(N,R,O,Y,G,B,V):
  assert N==R+O+Y+G+B+V
  if V>Y or G>R or O>B: return "IMPOSSIBLE"
  if V==Y and V>0:
    if V+Y<N: return "IMPOSSIBLE"
    return "VY"*V
  if G==R and G>0:
    if G+R<N: return "IMPOSSIBLE"
    return "GR"*G
  if O==B and B>0:
    if B+O<N: return "IMPOSSIBLE"
    return "BO"*O
  Y-=V;R-=G;B-=O
  mx=max(R,Y,B)
  if 2*mx>R+Y+B: return "IMPOSSIBLE"
  s=""
  while R+Y+B>0:
    assert R>=0 and Y>=0 and B>=0
    if s=="":
      if R>=Y and R>=B: s+='R';R-=1;continue
      if Y>=R and Y>=B: s+='Y';Y-=1;continue
      s+='B';B-=1;continue
    if s[0]=='R' and s[-1]!='R' and R>0 and R+Y>=B and R+B>=Y: s+='R';R-=1;continue
    if s[0]=='B' and s[-1]!='B' and B>0 and B+R>=Y and B+Y>=R: s+='B';B-=1;continue
    if s[0]=='Y' and s[-1]!='Y' and Y>0 and Y+B>=R and Y+R>=B: s+='Y';Y-=1;continue
    if s[-1]=='R':
      if Y>=B: s+='Y';Y-=1;continue
      s+='B';B-=1;continue
    if s[-1]=='Y':
      if R>=B: s+='R';R-=1;continue
      s+='B';B-=1;continue
    if s[-1]=='B':
      if R>=Y: s+='R';R-=1;continue
      s+='Y';Y-=1;continue
    assert 0
  s=s.replace('R','RG'*G+'R',1)
  s=s.replace('Y','YV'*V+'Y',1)
  s=s.replace('B','BO'*O+'B',1)
  return s

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,R,O,Y,G,B,V]=[int(y) for y in sys.stdin.readline().strip().split()]
  print "Case #%d:"%case,thing(N,R,O,Y,G,B,V)
