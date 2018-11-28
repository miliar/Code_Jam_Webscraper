t = int(raw_input())

def tidy(check):
    check=str(check)
    s=1
    tidyy=True
    while s<len(check):
        if (check[s]<check[s-1]):
            tidyy=False
        s+=1
    return tidyy

for i in xrange(1, t + 1):
  n=int(raw_input())
  c=n
  while True:
      if tidy(c):
          print ("Case #{}: {}".format(i, c))
          break
      c-=1
