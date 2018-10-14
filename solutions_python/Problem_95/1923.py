import sys
sys.stdin = open("data.in", "r")
sys.stdout = open("data.out", "w")
i = 1
t = int(input())
map = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}
while i <= t:
  inp = input()
  out = []
  for c in inp:
      out.append(map[c])
  print("Case #%d: %s" % (i, "".join(out)))
  i += 1
