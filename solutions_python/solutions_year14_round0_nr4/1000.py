import sys

def main():
  readInput()

def readInput():
  i = sys.stdin
  o = ""
  if len(sys.argv) >= 2:
    fn = sys.argv[1]
    if fn != "-":
      i = open(fn)
      o = open(fn.replace("in", "out"), "w")

  cases = int(i.readline())
  for c in range(cases):
    blocks = int(i.readline())
    naomi = i.readline()
    ken = i.readline()
    o.write("Case #%i: %s\n" % (c + 1, calcScorePoints(naomi, ken)))
  i.close()
  o.close()

def calcScorePoints(naomio, keno):
  naomi = [float(n) for n in naomio.split(" ")]
  naomi.sort()
  ken = [float(k) for k in keno.split(" ")]
  ken.sort()

  deceitfulWar = 0
  originalWar = 0

  #deceitfulWar
  for n in naomi:
    if n > ken[0]:
      del(ken[0])
      deceitfulWar += 1
    else:
      del(ken[-1])

  naomi = [float(n) for n in naomio.split(" ")]
  naomi.sort()
  ken = [float(k) for k in keno.split(" ")]
  ken.sort()

  for n in naomi:
    #originalWar
    i = 0
    for k in ken:
      if k > n:
        break
      i += 1
    if i < len(ken):
      del(ken[i])
    else:
      del(ken[0])
      originalWar += 1

  return "%i %i" % (deceitfulWar, originalWar) 

if __name__ == "__main__":
  main()
