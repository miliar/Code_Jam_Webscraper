
def get_lim(n):
  s = str(n)
  l = len(s)
  low_lim = '1'
  
  digit = s[0:1]
  mask = digit
  #print("digit {0}".format(digit))
  
  for i in range(1, l):
    mask += digit
  
  return mask


def calc(n):
  res = 0
  s = str(n)
  l = len(s)
  limit = int(get_lim(n))
  if l == 1:
    return int(n)
  
  #print("mask: {0}".format(limit))
  
  if n == limit:
    res = limit
  
  if n < limit:
    rem = s[1:]
    res = n - (int(rem)+1)
      
  if n > limit:
    res = int(s[0:1])*10**(l-1)
    if l > 2:
      for i in range(1, l-1):
        n1 = s[i:]
        res += calc(int(n1))
    else:
      n1 = s[1:]
      res += calc(int(n1))
  
  return res
  
  
def main():
  #f = open('input', 'r')
  f = open('B-small-attempt4.in', 'r')
  lines = f.readlines()
  f1 = open('output', 'a')
  t = int(lines[0])
  
  for i in range(1, t+1):
    line = lines[i]
    #print(int(line))
    res = calc(int(line))
    f1.write('Case #{0}: {1}\n'.format(i, res))
    #print('Case #{0}: {1}\n'.format(i, res))


if __name__=="__main__":
  main()
