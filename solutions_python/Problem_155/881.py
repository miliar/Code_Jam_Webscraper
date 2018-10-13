infile = 'A-large.in'
outfile = 'A-large-out.txt'

def need(n):
  add = 0
  standing = n[0]
  for i in xrange(1, len(n)):
    if n[i] > 0 and i > standing:
      diff = i - standing
      add += diff
      standing += diff
    standing += n[i]
  return add
      
def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    a = [int(i) for i in f.readline().split()[1]]
    out.write("Case #"+str(n+1)+": "+str(need(a))+"\n")


main()

