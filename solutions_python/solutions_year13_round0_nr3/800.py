def is_square(a):
  if a == 1:
    return [True, 1]
  x = a // 2 
  seen  = set([x])
  while x * x != a:
    x = (x + (a//x)) // 2
    if x in seen:
      return [False, x]
    seen.add(x)
  return [True, x]

def isPalin(a):
    s = str(a)
    for i in range(len(s)//2):
      if s[i] != s[-i-1]:
        return False
    return True

def solve():
#  f = open("in.txt", 'r')
  f = open("C-small-attempt0.in")
#  f = open("C-large-in")
  T = int(f.readline())
  for i in range(T):
    l = f.readline()
    [sA, sB] = l.split()
    A = int(sA)
    B = int(sB)
    count = 0
    [bA, rA] = is_square(A)
    [bB, rB] = is_square(B)
    for j in range(rA, rB+1):
      jsq = j*j
      if jsq>=A and jsq <=B:
         if isPalin(j) and isPalin(jsq):
           count += 1
    print "Case #%i: %i" % ((i+1),count)

solve()
