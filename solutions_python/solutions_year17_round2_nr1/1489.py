t = int(input())

for z in range(t):
  d,n=[int(n) for n in (input().split(' '))]
  ks=[]
  for y in range(n):
    kt,st=[int(n) for n in input().split(' ')]
    ks.append([kt,st])
  time=0
  td=0
  for x in ks:
    td = x[0] +x[1]*time
    if td>d:
      continue
    time = time + ((d-td)/x[1])
  r = (d/time)
  print ("Case #{}: {}".format(z+1,r))