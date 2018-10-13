def main():
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    for s in input().split(" "):
      n = int(s)
    a = splitInt(n)
    x = 0
    while x == 0:
      x = compareList(n,a)
      if x == 0:
        n -= 1
        a = splitInt(n)
    print("Case #{}: {}".format(i, n))


def splitInt(n):
  a = []
  while (n//10 != 0):
    b = n%10
    a.append(b)
    n = n//10
  b = n%10
  a.append(b)
  return a

def compareList(n,a):
  for idx, elem in enumerate(a):
    thiselem = elem
    if idx+1 == len(a):
      break
    nextelem = a[(idx + 1) % len(a)]
    if thiselem < nextelem:
      return 0
  return n



if __name__ == '__main__': 
  main()