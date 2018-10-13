t = int(input())

i = 1
while i<=t:
  n,k = [int(x) for x in input().split()]

  stalls = [0,n+1]

  while k>0:
    l = len(stalls)
    diff = []
    for a in range(l-1):
      diff.append(stalls[a+1]-stalls[a])

    max_val = max(diff)
    max_index = diff.index(max_val)

    val = int((max_val/2))+stalls[max_index]
    stalls.append(val)

    stalls.sort()
    k = k-1

  ind = stalls.index(val)

  mxs = max([val-stalls[ind-1],stalls[ind+1]-val])-1
  mns = min([val-stalls[ind-1],stalls[ind+1]-val])-1

  print("Case #{}: {} {}".format(i,mxs,mns))

  i = i+1
