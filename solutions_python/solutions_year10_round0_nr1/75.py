input = open('1.in', 'r')
output = open('1.out', 'w')
n = int(input.readline())
for i in range(1,n+1):
  (N,K) = input.readline().split(' ')
  (N,K) = ((int(N), int(K)))
  if 0 == (K+1) % pow(2,N):
      print "%d %d ON" % (N,K)
      output.write('Case #' + str(i) + ": ON\n")
  else:
      print "%d %d OFF" % (N,K)
      output.write('Case #' + str(i) + ": OFF\n")

