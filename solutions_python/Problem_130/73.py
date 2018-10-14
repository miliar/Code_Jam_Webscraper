import math

fin = open('in2.txt','r')
fout = open('out2.txt','w')

T = int(fin.readline().strip())

#Functions in here

for idx in range(T):
  N,P = [long(a) for a in fin.readline().strip().split(' ')]
  #optimistic
  optimistic_wins = 0
  for k in range(N+1):
    if 2**(N-k)-1<P:
      optimistic_wins = k
      break
  optimistic_winner = 2**N-2**optimistic_wins
  #pessimistic
  pessimistic_losses = N-1
  pessimistic_winner = None
  print "N,P",N,P
  for k in range(N+1):
    if (2**k-1)*2**(N-k)>=P:
      pessimistic_losses = k-1
      break
  else:
    pessimistic_winner = 2**N-1
  if pessimistic_winner is None:
    pessimistic_winner = 2**(pessimistic_losses+1)-2
  ans = str(pessimistic_winner) + " " + str(optimistic_winner)
  out = "Case #" + str(idx+1) + ": " + ans + "\n"
  fout.write(out)

fin.close()
fout.close()
