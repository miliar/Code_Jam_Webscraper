
T = int(input())

for t in range(1, T+1):
  ans = [0]*2
  arr = [[]] * 2

  for i in [0, 1]:
    ans[i] = int(input())
    
    for j in [1,2,3,4]:
      if j == ans[i]:
        arr[i] = set(map(int, input().split(" ")))
      else:
        input()
   
  sol = "Bad magician!"
  intersection = arr[0] & arr[1]
  if len(intersection) == 1:
    sol = list(intersection)[0]
  elif len(intersection) == 0:
    sol = "Volunteer cheated!"

  print("Case #%i:" % t, sol)
