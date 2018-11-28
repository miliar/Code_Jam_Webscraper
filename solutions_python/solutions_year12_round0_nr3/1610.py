import itertools
T = int(raw_input())
for i in range(T):
  a,b = raw_input().split()
  a = int(a)
  b = int(b)
  num_set = [x for x in range((a),(b)+1)]
  count = 0
  while num_set:
    x = num_set[0]
    subset = set([x])
    num_len = len(str(x))
    number = x
    for y in range(num_len - 1):
      rem = number%10
      number = number/10
      number += rem * pow(10,num_len-1)
      subset.add(number)
    subset = set([ x for x in subset if (x>=a and x<=b) ])
    for x in subset:
      if x in num_set:
        num_set.remove(x)
    if len(subset)>1:
      count = count + len(list(itertools.combinations(subset,2))) 
  print "Case #" + str(i+1) + ": " + str(count)
