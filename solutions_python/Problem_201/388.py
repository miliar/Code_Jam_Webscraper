def place_in_order(list,elem):
  k = len(list)-1
  while list[k] < elem:
    k -= 1
  if list[k] > elem:
    list.insert(k+1,elem)
  return list

def add_to(dict,elem,amount):
  if elem in dict:
    dict[elem] += amount
  else:
    dict[elem] = amount
  return dict

t = int(input())
for i in range(1, t + 1):
  stalls, people = [int(s) for s in input().split(" ")]
  empty_stalls = {stalls: 1}
  keys = [stalls]
  while True:
    m = empty_stalls[keys[0]]
    if m >= people:
      break
    people -= m
    if keys[0] % 2 == 1:
      empty_stalls = add_to(empty_stalls,keys[0]//2,m*2)
      keys = place_in_order(keys,keys[0]//2)
    else:
      empty_stalls = add_to(empty_stalls,keys[0]//2,m)
      empty_stalls = add_to(empty_stalls,keys[0]//2-1,m)
      keys = place_in_order(keys,keys[0]//2)
      keys = place_in_order(keys,keys[0]//2-1)
    del(keys[0])
  print("Case #{}: {} {}".format(i, keys[0]//2, keys[0]//2-1+(keys[0]%2)))
  