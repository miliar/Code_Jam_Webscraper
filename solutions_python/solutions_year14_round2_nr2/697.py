import fileinput
import sys

def test(n, a, b, k):
  counter = 0
  for i in range(a):
    for j in range(b):
      if i < k or j < k:
        counter += 1
      else:
        if i & j < k:
          counter += 1
  print "Case #" + str(n) + ": " + str(counter)
  return

def main():
  n = 0
  with open("B-small-attempt1.in") as fp:
    for line in fp:
      n += 1
      strs = line.split()
      a = int(strs[0])
      b = int(strs[1])
      k = int(strs[2])
      test(n, a,b,k)

if __name__ == "__main__":
    main()
