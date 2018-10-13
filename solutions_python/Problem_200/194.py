file_in = open('B-large.in', 'r')
file_out = open('b.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  n = list(file_in.readline().strip())
  n = [int(i) for i in n]

  i = 1
  k = None
  while(i < len(n)):
    if(n[i] < n[i-1]):
      k = i
      n[i-1] -= 1
      break
    i += 1

  while(i < len(n)):
    n[i] = 9
    i += 1

  if k is not None:
    while(k > 1):
      k -= 1
      if(n[k] < n[k-1]):
        n[k] = 9
        n[k-1] -= 1
      else:
        break

  while n[0] is 0:
    n.pop(0)
  
  n = [str(i) for i in n]
  ans = ''.join(n)

  file_out.write("Case #{}: ".format(t))
  file_out.write(ans)
  file_out.write('\n')