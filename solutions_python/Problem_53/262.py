import sys

def calc(n, k):
  if k == 0: return False
  return k % (2**n) == 2**n - 1

def main():
  ncases = int(sys.stdin.readline())
  for i in range(ncases):
    n, k = map(int, sys.stdin.readline().split())

    print("Case #%d: %s" % (i+1, "ON" if calc(n, k) else "OFF"))

main()
