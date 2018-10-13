file_in = open('A-large.in')
file_out = open('A-large.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  D, N = map(int, file_in.readline().split())
  # pos = []
  # spd = []
  ans = 999999999999999999999
  # p, s = 0,0
  for i in range(N):
    p, s = map(int, file_in.readline().split())
    if D > p:
      ans = min(ans, float(D*s) / float(D - p))
    # pos.append(p)
    # spd.append(s)
  # if ans == 999999999999999999999: print(D, N, p, s)
  file_out.write('Case #' + str(t) + ': ' + '{:.6f}'.format(ans) + '\n')
