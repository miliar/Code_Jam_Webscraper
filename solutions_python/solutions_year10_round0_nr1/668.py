def readi():
  return int(input())

def readf():
  return float(input())

def reada(f):
  return [f(x) for x in input().split()]

def readai():
  return reada(int)

def case():
  (N, K) = readai()
  shift = (1 << N) - 1
  temp = K & shift
  if (temp == shift):
    return "ON"
  else:
    return "OFF"

for N in range(readi()):
  result = case()
  print("Case #{0}: {1}".format(N + 1, result))
