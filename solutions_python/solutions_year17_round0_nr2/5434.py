def is_tidy(n):
  s = str(n)
  for i in range(len(s)-1):
    if s[i] > s[i+1]:
      return False
  return True

def bf_last_tidy(n):
  m = n
  while(not is_tidy(m)):
    m -= 1
  return m

def main(): 
  t = int(input())
  for i in range(1, t+1):
    [n] = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, bf_last_tidy(n)))

if __name__ == '__main__': main()