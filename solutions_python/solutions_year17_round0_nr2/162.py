def solve(f):
  x = f.readline().rstrip()
  i = 0
  while i < len(x)-1:
    if x[i]>x[i+1]:
      break
    i += 1
  if i==len(x)-1:
    return x
  i -= 1
  while i>=0 and x[i]==x[i+1]:
    i -= 1
  i += 1
  x = list(x)
  x[i] = `int(x[i])-1`
  i += 1
  while i<len(x):
    x[i] = '9'
    i += 1
  x = "".join(x)    
  return `int(x)`.rstrip('L')
  
def out(s):
  print s
  o.write(s)
  
f = open("i.in")
o = open("o.out", "wt")
T = int(f.readline())
for t in range(T):
  out("Case #%d: %s" %(t+1,solve(f)))
  o.write('\n')
o.close()