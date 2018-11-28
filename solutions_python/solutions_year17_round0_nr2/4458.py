import sys

def is_tidy(n):
  if n//10==0:
    return True
  else:
    s = str(n)
    res = True
    for i in range(len(s)-1):
      if int(s[i])>int(s[i+1]):
        res = False
    return res
    
def sol(n):
  if is_tidy(n):
    return n
  else:
    return sol(n-1)

f=open('solution.txt','w')
with open(sys.argv[1]) as fh:
    N = int(next(fh))
    i = 1
    for line in fh:
        print("Case #{}: {}".format(i, sol(int(line))),file=f)
        i += 1

f.close
