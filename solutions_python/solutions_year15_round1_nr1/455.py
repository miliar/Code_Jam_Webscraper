infile = 'A-large.in'
outfile = 'A-large-out.txt'

def process(mushs):
  m1 = 0
  m2 = 0
  mush_prev = mushs[0]
  maxDiff = 0
  for i in xrange(1, len(mushs)):
    mush_this = mushs[i]
    if mush_this < mush_prev:
      diff = mush_prev - mush_this
      m1 += diff
      if diff > maxDiff:
        maxDiff = diff
    mush_prev = mush_this
  for i in xrange(len(mushs)-1):
    m2 += min(maxDiff, mushs[i])
  return m1, m2
         
  
      
def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    b = f.readline()
    a = [int(i) for i in f.readline().split()]
    m1, m2 = process(a)
    out.write("Case #"+str(n+1)+": "+str(m1)+" "+str(m2)+"\n")


main()

