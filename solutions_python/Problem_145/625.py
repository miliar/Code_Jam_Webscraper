import math

def gcd(a, b):
  b, a = sorted([a,b])
  while b > 0:
    a, b = b, a % b
  return a

def x(a, b):
  c = gcd(a, b)
  a, b = a//c, b//c # simplify
  
  ex = math.log(b, 2)
  if ex != int(ex): # pow2
    return False

  ex = int(ex)

  i = 0
  while a > 1:
    i += 1
    a = a >> 1

  return ex-i
  
def main():
  N = int(input())
  for i in range(1,N+1):
    a, b = map(int, input().split("/"))
    y = x(a,b)
    print('Case #{}: {}'.format(i, y if y is not False else 'Impossible'))

main()

