def process_small(P, X):
  joint = 1.0
  N = len(P)
  P = list(reversed(sorted(P)))
  sumP = sum(P)

  if sumP + X >= N:
    return 1.0

  acc = 1.0

  for i in range(N):
    if (sumP + X)/(N-i) >= P[i]:
      return acc*pow((sumP + X)/(N-i), N-i)
    else:
      sumP -= P[i]
      acc *= P[i]
  return acc


def run():
  T = int(raw_input().strip())

  for caseno in xrange(T):
    N, K = map(int, raw_input().strip().split())
    X = float(raw_input().strip())
    P = map(float, raw_input().strip().split())

    answer = process_small(P, X)
    print "Case #" + str(caseno+1) + ": " + '{:.10f}'.format(answer)

# print process_small([0.8, 0.9], 0.15)

run()