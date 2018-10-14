

T = int(input())
for test in range(1, T+1):
   line = input().split()
   a = int(line[0])
   b = int(line[1])
   nb = 0
   i = 1
   m = 1
   while m*m <= b:
      if m*m >= a and str(m*m)[::-1] == str(m*m):
         nb = nb + 1
      x = bin(i)[2:]
      m = (10**len(x))*int(x) + int(x[::-1])
      i = i + 1
   i = 2 
   m = 10
   while m*m <= b:
      if m*m >= a and str(m*m)[::-1] == str(m*m):
         nb = nb + 1
      x = bin(i)[2:]
      m = (10**(len(x) - 1))*int(x) + int(x[1::-1])
      i = i + 1
   i = 1
   m = 2
   while m*m <= b:
      if m*m >= a and str(m*m)[::-1] == str(m*m):
         nb = nb + 1
      i = i*10
      m = 2*i+2
   if(a <= 94249 and b >= 94249):
      nb = nb + 1
   if(a <= 9 and b >= 9):
      nb = nb + 1
   print('Case #{}: {}'.format(test, nb))

   
