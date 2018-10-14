import sys

def main():
  readInput()

def readInput():
  i = sys.stdin
  if len(sys.argv) >= 2:
    fn = sys.argv[1]
    if fn != "-":
      i = open(fn)

  cases = int(i.readline())
  for c in range(cases):
    magician = []
    for t in range(2):
      v = int(i.readline())
      for w in range(v - 1):
        i.readline()
      magician.append(i.readline())
      for w in range(4 - v):
        i.readline()
    print "Case #%i: %s" % (c + 1, generateOutput(magician))

def generateOutput(magician):
  x = set([int(n) for n in magician[0].split(" ")])
  y = set([int(n) for n in magician[1].split(" ")])
  s = x&y
  if len(s) == 1:
    return str(list(s)[0])
  elif len(s) >= 1:
    return "Bad magician!"
  else:
    return "Volunteer cheated!"

if __name__ == "__main__":
  main()
