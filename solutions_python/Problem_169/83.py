f = open('B-small-attempt0.in')
o = open('output.txt', 'w')
n = int(f.readline())
for i in range(n):
  y, v, x = [float(a) for a in f.readline().strip().split(" ")]
  y = int(y)
  arr = []
  for j in range(y):
    arr.append([float(a) for a in f.readline().strip().split(" ")])
  ans = "IMPOSSIBLE"
  if y == 1 and arr[0][1] == x:
    ans = v/arr[0][0]
    #print ans
  if y== 2:
    if max(arr[0][1], arr[1][1]) >= x and min(arr[0][1], arr[1][1]) <= x:
      #print arr
      if arr[1][1] == arr[0][1]:
        ans = v/(arr[1][0]+arr[0][0])
      else:
        t_1 = v*(x-arr[0][1])/arr[1][0]/(arr[1][1]-arr[0][1])
        t_0 = (v-arr[1][0]*t_1)/arr[0][0]
        ans = max(t_1, t_0)
  o.write('Case #'+str(i+1)+': '+str(ans)+'\n')
f.close()
o.close()