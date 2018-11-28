import sys

def main():
  ncases = int(input())
  for cc in range(ncases):
    n, m = map(int, input().split())

    exist = set([])
    for i in range(n):
      s = input()
      assert s[0] == '/'
      xs = s[1:].split('/')
      for j in range(1, len(xs)+1):
        exist.add("/".join(xs[:j]))

    ans = 0
    for i in range(m):
      s = input()
      assert s[0] == '/'
      xs = s[1:].split("/")
      for j in range(1, len(xs)+1):
        dir = "/".join(xs[:j])
        if dir not in exist:
          ans += 1
          exist.add(dir)

    print("Case #%s: %s" % (cc+1, ans))

main()
