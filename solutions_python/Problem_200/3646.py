def tidyup(arr, start, l):
    arr[start-1] = arr[start-1] - 1
    while start < l:
        arr[start] = 9
        start += 1

def tidy(i):
    n = [int(i) for i in list(str(i))]
    j = 1
    l = len(n)
    while j < l:
        if n[j] < n[j-1]:
            return False
        j += 1
    return True
    
def tidydumb(i):
    while not tidy(i):
        i -= 1
    return i
        
def tidysmart(i):
  num = [int(x) for x in str(i).strip()]
  j = 1
  l = len(num)
  while j < l:
      if num[j] < num[j-1]:
          while j > 1 and num[j-1] == num[j-2]:
              j -= 1
          tidyup(num, j, l)
          break
      j += 1
  if num[0] == 0:
      num = num[1:]
  return int("".join([str(n) for n in num]))
        
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  our = tidysmart(n)
  print("Case #{}: {}".format(i, our))
