infile = 'D-large.in'
outfile = 'D-large-out0.txt'
# outfile = 'D-small-try.txt'

# a1 = "0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899".split()
# a2 = "0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458".split()
# a1 = [float(i) for i in a1]
# a2 = [float(i) for i in a2]
# a1.sort()
# a2.sort()
def warBest(a1, p2):
  a2 = list(p2)
  points = 0
  while len(a1) > 0:
    if a1[-1] > a2[-1]: # P1 is going to win
      points += 1      
      a2 = a2[1:]
    else: # P2 is going to win
      a2.pop([i for i in range(len(a2)) if a2[i] > a1[-1]][0])
    a1 = a1[:-1]
  return points

def DwarBest(p1,p2):
  a1 = list(p1)
  a2 = list(p2)
  points = 0
  while len(a1) > 0:
    if a1[0] > a2[0]:
      points += 1
      a2.pop(0)
    else:
      a2.pop()
    a1.pop(0)
  return points

def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    f.readline()
    p1 = [float(i) for i in f.readline().split()]
    p2 = [float(i) for i in f.readline().split()]
    p1.sort()
    p2.sort()
    out.write("Case #"+str(n+1)+": "+str(DwarBest(p1,p2))+" "+str(warBest(p1,p2))+" "+"\n")

main()
