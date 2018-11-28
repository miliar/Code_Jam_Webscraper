

testnum = int(input())
for i in range(1, testnum+1):
  arr = [int(x) for x in list(input())]
  
  k = -1
  for j in range(len(arr)-1):
    if (arr[j] > arr[j+1]):
      k=j+1
      break
  if k != -1:
    arr[k:] = [9]*(len(arr)-k)
    val = arr[k-1]
    if val == 1:
      arr[:k] = [9]*(k-1)
    else:
      j = k-1
      while j>=0 and arr[j] == val:
        arr[j] = 9
        j-=1
      arr[j+1] = val-1
      
  finaltidy = ''.join([str(x) for x in arr])
  print("Case #"+str(i)+":", finaltidy)