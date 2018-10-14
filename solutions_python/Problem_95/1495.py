inp = open('./A-small.in', 'r')
outp1 = open('./out1.txt', 'w')
outp2 = open('./out2.txt', 'w')

T = int(inp.readline())

s = 'abcdefghijklmnopqrstuvwxyz '
t1 = 'ynficwlbkuomxsevqpdrjgthaz '
t2 = 'ynficwlbkuomxsevzpdrjgthaq '

def solve(i):
  S = inp.readline()
  outp1.write('Case #' + str(i) + ': ')
  outp2.write('Case #' + str(i) + ': ')
  for i in S:
    outp1.write(s[t1.find(i)])
    outp2.write(s[t2.find(i)])
  outp1.write('\n')
  outp2.write('\n')

for k in range(T):
  solve(k+1)

inp.close()
outp1.close()
outp2.close()
 