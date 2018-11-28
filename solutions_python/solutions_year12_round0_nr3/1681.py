T = int(raw_input())

for i in range(T):
  I = raw_input()
  I = I.split()

  A = int(I[0])
  B = int(I[1])
  
  count = 0

  for j in range(A, B+1):
    n = j
    
    num = str(n)
    for k in range(1, len(num)):
      x = num[-(k):] + num[:len(num)-k]
      m = int(x)

      if A<=n and n<m and m<=B:
        count = count + 1

  print 'Case #' + str(i+1) + ': ' + str(count)
