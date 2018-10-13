T = int(input())

def solve0(R, Y, B):
  b = B-(R-Y)
  return "ryb"*b+"ry"*(Y-b)+"rb"*(R-Y)

def solve1(N, R, Y, B):
  if R>N/2 or Y>N/2 or B>N/2:
    return "IMPOSSIBLE"
  # colors = [[R, 'R'], [Y, 'Y'], [B, 'B']]
  # colors = {'R': R, 'Y': Y, 'B': B}
  # alphabet = set(['R', 'Y', 'B'])
  # c = sorted(colors.items(), key=lambda x: x[1])[0][1]
  # ans = []
  # while N:
  #   ans.append(c)
  #   N-=1
  #   c__=None
  #   for c_ in alphabet:
  #     if c__ is None or c_!=c and c__ = 
  #     colors[c_]


  #   colors[0][0]-=1
  #   N-=1
  if R>=Y and R>=B:
    return solve0(R,Y,B).replace('r', 'R').replace('y', 'Y').replace('b', 'B')
  if Y>=R and Y>=B:
    return solve0(Y, R, B).replace('r', 'Y').replace('y', 'R').replace('b', 'B')
  if B>=Y and B>=R:
    return solve0(B, Y, R).replace('r', 'B').replace('y', 'Y').replace('b', 'R')

def solve2(N, R, O, Y, G, B, V):
  r = R-G; y = Y-V; b = B-O;
  if r==0 and y==0 and b==0:
    if len(list(filter(lambda x: x!=0, [R, Y, B])))>1:
      return "IMPOSSIBLE"
    else:
      if R!=0:
        return "RG"*R
      if Y!=0:
        return "YV"*Y
      if B!=0:
        return "BO"*B
  ans1 = solve1(r+y+b, r, y, b)
  if ans1=="IMPOSSIBLE":
    return ans1
  return ans1.replace('R', 'RGR', G).replace('Y', 'YVY', V).replace('B', 'BOB', O)

for i in range(1,T+1):
  N, R, O, Y, G, B, V = map(int, input().split(' '))
  print("Case #{}: {}".format(i, solve2(N, R, O, Y, G, B, V)))







