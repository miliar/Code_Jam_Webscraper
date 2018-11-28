import sys

def func(f, c, x, k):
  return sum([c / (2.0 + i * f) for i in range(k)] + [x / (2.0 + k * f)])

with open(sys.argv[1], 'r') as inp, open(sys.argv[2], 'w') as outp:
  casos = int(inp.readline())
  for caso in range(casos):
    c, f, x = map(float, inp.readline().split())
    best = 500000.0
    for k in range(2000):
      best = min(best, func(f, c, x, k))
    outp.write("Case #%d: " % (caso + 1) + str(best) + "\n")
