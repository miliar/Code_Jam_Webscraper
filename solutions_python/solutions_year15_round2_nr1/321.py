def reverse(n):
  return int(str(n).strip('0')[-1::-1])

def process(n):
  steps = range(0, n+1)
  rev = range(0, n+1)
  for i in xrange(1, n+1):
    steps[i] = min(steps[i], steps[i-1]+1)
    #for j in xrange(0, i):
    #  steps[i] = min(steps[i], i-j+steps[j])
    rev[i] = reverse(i)
    if rev[i] > i and rev[i] <= n:
      forward = rev[i]
      steps[forward] = min(steps[forward], steps[i]+1)
  #print steps
  return steps[n] 

def main():
  tC = int(input())
  tc = tC
  while tc > 0:
    tc -= 1
    n = int(input())
    ans = process(n)
    print u"Case #{}: {}".format(tC-tc, ans)

if __name__ == "__main__":
  main()
