def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    a,n = map(int, input().split())
    ls = list(map(int, input().split()))
    if a == 1:
      print("Case #%i: %i" % (caseNr, n))
    else:
      print("Case #%i: %i" % (caseNr, solve(a,0,sorted(ls))))
    
def solve(a, i, ls):
  if i >= len(ls):
    return 0
  else:
    if ls[i] < a:
      # print('ok',a,i,ls[i])
      return solve(a+ls[i],i+1,ls)
    else:
      # print('no_ok',a,i,ls[i])
      to_remove = len(ls)-i
      to_add = will_add(a,i,ls)
      # print('to_add', to_add)
      # print('to_remove', to_remove)
      if to_add<to_remove:
        (to_add_now,new_a) = need_to_add(a,ls[i])
        # print('to_add',a,i,ls[i],to_add,to_add_now)
        # print('to_add_now', to_add_now)
        return to_add_now + solve(new_a,i+1,ls)
      else:
        # print('to_remove',a,i,ls[i],to_remove)
        return to_remove
          
def need_to_add(a,v):
  added = 0
  while v >= a:
    added+=1
    a+=a-1
  return (added,a+v)
  
def will_add(a,i,ls):
  if i >= len(ls):
    return 0
  else:
    # print('will_add',a,i,ls[i])
    if ls[i] < a:
      # print('ok',a,i,ls[i])
      return will_add(a+ls[i],i+1,ls)
    else:
      to_remove = len(ls)-i
      (to_add_now,new_a) = need_to_add(a,ls[i])
      to_add = to_add_now + will_add(new_a,i+1,ls)
      # print('else',to_remove,to_add)
      if to_add<to_remove:
        # print('to_add',a,i,ls[i],to_add,to_add_now)
        # print('to_add_now', to_add_now)
        return to_add
      else:
        # print('to_remove',a,i,ls[i],to_remove)
        return to_remove
      
    
if __name__ == "__main__":
  main()
    