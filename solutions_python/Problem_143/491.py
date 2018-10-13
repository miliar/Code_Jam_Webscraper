infile = 'B-small-attempt0.in'
outfile = 'B-small-out.txt'

def check(A, B, K):
  win = 0
  for a in xrange(A):
    for b in xrange(B):
      if a & b < K:
        win += 1
  return win

def main():
  out = open(outfile, 'w')
  with open(infile) as f:
    M = int(f.readline())
    for n in xrange(M):
      [A, B, K] = map(int, f.readline().split())
      out.write("Case #"+str(n+1)+": "+str(check(A,B,K))+"\n")
  out.close()


main()
