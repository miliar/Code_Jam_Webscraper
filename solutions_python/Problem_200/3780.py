def is_tidy(x):
  if to_list(x)==sorted(x):
    return True
  return False

def to_list(x):
  temp=[]
  for a in x:
    temp.append(a)
  return temp

t = int(input())
for z in range(t):
  n = int(input())
  if n<=int((len(str(n))-1)*'1'+'0'):
    print("Case #{}: {}".format(z+1,(len(str(n))-1)*'9'))
    continue;
  result=0
  b=n
  while (True):
    if is_tidy(str(b)):
      result=b
      break
    b=b-1
  print("Case #{}: {}".format(z+1,result))
    

  