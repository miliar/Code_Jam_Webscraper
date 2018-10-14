T = int(input())

def solve(P, G):
  p = []
  for i in range(P):
    p.append(len([g for g in G if g%P==i]))
  if P==2:
    return p[0]+(p[1]+1)//2
  if P==3:
    min_=min(p[1], p[2])
    diff = abs(p[1]-p[2])
    return p[0]+min_+(diff+2)//3
  if P==4:
    b2 = p[2]%2
    min_=min(p[1], p[3])
    diff = abs(p[1]-p[3])
    if b2:
      others = (diff+5)//4
    else:
      others = (diff+3)//4
    return p[0]+p[2]//2+min_+others

for i in range(1,T+1):
  N, P = map(int, input().split(' '))
  G = list(map(int, input().split(' ')))
  print("Case #{}: {}".format(i, solve(P, G)))