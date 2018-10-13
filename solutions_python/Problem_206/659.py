from __future__ import division

def A(D, N, horses):
  max_time = 0
  for h in horses:
    K = h[0]
    S = h[1]
    time = (D-K)/S
    if time > max_time:
      max_time = time
  speed = D/max_time

  return str(speed)
  
def Parse():
  fin = open(r"D:\Projects\Python\Google\Round1B\A-large.in", 'r')
  fout = open(r"D:\Projects\Python\Google\Round1B\A-large.out", 'w')
  count = int(fin.readline())
  for i in range(1, count+1):
    line = [int(s) for s in fin.readline().split(" ")]
    D = line[0]
    N = line[1]
    horses = []
    for j in range(0, N):
      line = [int(s) for s in fin.readline().split(" ")]
      K = line[0]
      S = line[1]
      horses.append((K, S))

    ret = A(D, N, horses)
    result = "Case #%d: %s\n" % (i, ret)
    print result
    fout.write(result)
  fin.close()
  fout.close()

Parse()