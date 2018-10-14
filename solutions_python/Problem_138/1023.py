import sys
def war(nao, ken):
  w_opt = 0
  while ken:
    if nao[0] < ken[0]:
      nao = nao[1:]
      ken = ken[1:]
    else:
      ken = ken[1:]
      w_opt += 1
  return w_opt

def dwar(nao,ken):
  dw_opt = 0
  while ken:
    if nao[-1] > ken[-1]:
	dw_opt += 1
        nao = nao[:-1]
        ken = ken[:-1]
    else:
        nao = nao[1:]
        ken = ken[:-1]
  return dw_opt

def solution(f):
  f.readline()
  nao = sorted(map(float, f.readline().split()))
  ken = sorted(map(float, f.readline().split()))
  
  return "{} {}".format(dwar(nao, ken), war(nao, ken))

f = sys.stdin
T = int(f.readline())
for x in range(T):
  print "Case #{}: {}".format((x + 1), solution(f))
