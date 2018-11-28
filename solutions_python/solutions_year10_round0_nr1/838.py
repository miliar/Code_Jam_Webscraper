#f = open('a.in')
f = open('/Users/simple/Desktop/A-large.in.txt')
N = int(f.readline())
for i in range(N):
  N, K = map(int, f.readline().split())
  s = [0] * N
#  print('N=',N)
  if (K + 1) % (2 ** N) == 0:
    result = 'ON'
  else:
    result = 'OFF'
#  result = 'OFF' if 0 in s else 'ON'
  print('Case #{0}: {1}'.format(i+1,result))
#
#  print(s)
      

