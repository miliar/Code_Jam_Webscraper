def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    c,f,x = map(float, input().split())
    print("Case #%i: %f" % (caseNr, solve(c,f,x)))
  
def solve(c,f,x):
  p = 2
  t = 0
  while 1:
    t1 = x / p
    t2 = c / p + x / (p+f)
    if ( t1 < t2 ):
      return t1+t
    else:
      t = t + c/p
      p += f
  
if __name__ == "__main__":
  main()
