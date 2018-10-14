infile = 'B-small-attempt0.in'
outfile = 'B-small-out.txt'

def farmTime(t, C, F, X):
  sums = 0
  for i in xrange(t-1):
    sums += C/(2+F*i)
  sums += X/(2+F*(t-1))
  return sums

def main():
  out = open(outfile, 'w')
  with open(infile) as f:
    N = int(f.readline())
    for n in xrange(N):
      [C, F, X] = [float(i) for i in f.readline().split()]
      time = farmTime(1, C, F, X)
      t = 2
      while True:
        time2 = farmTime(t, C, F, X)
        if time2 < time:
          time = time2
          t += 1
        else:
          break
      out.write("Case #"+str(n+1)+": "+str(round(time,7))+"\n")


main()

