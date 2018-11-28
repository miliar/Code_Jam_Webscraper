def works(A, x):
  for num in A:
    if x % num != 0 and num % x != 0:
      return False
  return True

def main():
  T = int(raw_input())
  for t in range(1, T+1):
    N, L, H = map(int, raw_input().split())
    A = map(int, raw_input().split())

    sol = None
    for i in range(L, H+1):
      if works(A, i):
        sol = i
        break
    print "Case #%d: %s" % (t, sol if sol else "NO")

if __name__ == '__main__':
  main()
