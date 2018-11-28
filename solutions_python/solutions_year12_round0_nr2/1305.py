inp = open('./B-large.in', 'r')
outp = open('small.out.txt', 'w')

T = int(inp.readline())

def solve(i):
  t = inp.readline().split(' ')
  N = int(t[0])
  S = int(t[1])
  p = int(t[2])
  t = [(int(x) - p) / 2 for x in t[3:]]

  d = len([x for x in t if x >= p-1])
  s = len([x for x in t if x == p-2 and x >= 0])
  d = d + min(s, S)

  outp.write('Case #' + str(i) + ': ' + str(d) + '\n')
    

for i in range(T):
  solve(i+1)

inp.close()
outp.close()