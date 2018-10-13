for t in range(1,input()+1):
  n = raw_input()
  n = map(int, n)
  for d in range(len(n)-1)[::-1]:
    if n[d] <= n[d+1]: continue
    n[d] -= 1
    n[d+1:] = [9]*(len(n)-d-1)
  print 'Case #%i:'%t, int(''.join(map(str,n)))
