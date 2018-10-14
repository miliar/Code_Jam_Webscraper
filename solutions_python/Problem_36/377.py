wcj = "welcome to code jam"

def count(s):
  old = [1]*(len(s)+1)
  for i, c in enumerate(wcj):
    new = [0]
    for j, sc in enumerate(s):
      if c == sc:
        new.append(new[j] + old[j])
      else:
        new.append(new[j])
      new[-1] = new[-1] % 10000
    old = new
  return new[-1]

inp = open('C-large.in.txt').readlines()[1:]
out= open('C-large.out','w')

for i, l in enumerate(inp):
    print >>out,"Case #%d: %04d" % (i+1, count(l[:-1]))
  


