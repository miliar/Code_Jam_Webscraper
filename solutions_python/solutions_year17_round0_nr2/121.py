


def last_tidy(n):
  p=0
  while  n > 10**(p+1):
    left = n // (10**p)
    right = n % (10**p)
    l=to_list(left)
    if not is_tidy(l):
      left = left-l[-1]-1
      n=left*10**p+right
    p+=1
  return n


def is_tidy(l):
  for i in range(1,len(l)):
    if l[i-1] > l[i]:
      return False
  return True

def to_list(n):
  l=[]
  while  n > 0:
    l.insert(0,n % 10)
    n=n//10
  return l


if __name__ == "__main__":
  t = int(input())
  for i in range(1, t + 1):
    n = int(input())
    res = last_tidy(n)
    print("Case #{}: {}".format(i, res))




