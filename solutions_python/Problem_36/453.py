import sys

def permutations(L, n):
    if n == 0:
        yield ""
    elif len(L) == n:
        yield L
    elif len(L) > n:
        (a, b) = (L[0:1], L[1:])
        for p in permutations(b, n):
            yield p
        for p in permutations(b, n-1):
            yield a + p

def memoize(f):
  memo = {}
  def inner(v1,v2):
      if not (v1,v2) in memo:
        memo[(v1,v2)] = f(v1,v2)
      return memo[(v1,v2)]
  return inner

#@memoize
def perm2(line, target):
    #while len(line) > len(target) and len(target) > 0 and line[0] != target[0]:
    #    line = line[1:]

    if len(line) < len(target):
        return 0
    elif len(line) == len(target):
        if line == target:
            return 1
        else:
            return 0
    elif len(target) == 0:
        if len(line) > 0:
            return 1
        else:
            return 0
    else:
        count = 0
        if line[0] == target[0]:
            count = perm2(line[1:], target[1:])
        count = count + perm2(line[1:], target)
        return count
        
        
            
            
infile = sys.stdin.readlines()
outfile = open("out.txt", "w")

TARGET = "welcome to code jam"

for (index ,line) in enumerate(infile[1:]):
    line = line.rstrip()
    ans = perm2(line, TARGET)
    print "answer: ", ans

    outfile.write("Case #%d: %04d\n"%(index+1, ans))
    




        
        
    


