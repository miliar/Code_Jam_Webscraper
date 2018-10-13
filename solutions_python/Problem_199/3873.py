import sys
sys.stdin = open("A-large.in")
sys.stdout = open("p1large.out", "w+")



def flip(n):
  if n==1:
    return 0
  else:
    return 1


for _ in range(int(input())):
  line, x = input().split()
  betterline = [0 for i in line]
  x = int(x)
  for i in range(len(line)):
    if line[i]=='+':
      betterline[i]=1
  
  count = 0
  for i in range(len(betterline)-x+1):
    if betterline[i] == 0:
      for j in range(x):
        betterline[i+j]=flip(betterline[i+j])
      count+=1
  
  
  #print(betterline)
  if 0 in betterline:
    print('Case #'+str(_+1)+': IMPOSSIBLE')
  else:
    print('Case #'+str(_+1)+': '+str(count))

sys.stdout.close()
