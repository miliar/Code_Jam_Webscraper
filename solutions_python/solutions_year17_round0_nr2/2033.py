tc = int(input())
def solve(n):
  ret = True
  prev = n[0]
  for i in range(1,len(n)):
    #print(prev , n[i],end= ' ')
    if prev > n[i]:
      ret = False
      break;
    prev = n[i]
  return ret 
for case in range(tc):
  n = int(input())
  for i in range(n,0,-1):
    if(solve(str(i))):
      break
  print("Case #{}: {}".format(case+1,i))