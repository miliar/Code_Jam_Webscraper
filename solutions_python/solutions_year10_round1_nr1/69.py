import sys,math
true,false = (1,0)
fin = open('A-large.in','r')
sys.stdout = open('A-large.out','w')

def isJoin(ch):
     count = 0
     for i in range(0,N):
          count = 0
          for j in range(0,N):
               if table[i][j] == ch: count+=1
               else: count = 0
               if count == K: return true
     for i in range(0,N):
          count = 0
          for j in range(0,N):
               if table[j][i] == ch: count+=1
               else: count = 0
               if count == K: return true
     #################
     for i in range(0,N):
          count = 0
          j = 0
          while i-j >= 0:
               if table[i-j][j] == ch: count+=1
               else: count = 0
               if count == K: return true
               j+=1
     for i in range(1,N):
          count = 0
          j = 0
          while i+j < N and N-j-1 >= 0:
               if table[N-1-j][i+j] == ch: count+=1
               else: count = 0
               if count == K: return true
               j += 1
     #################
     for i in range(0,N):
          count = 0
          j = 0
          while i+j < N:
               if table[j][i+j] == ch: count+=1
               else: count = 0
               if count == K: return true
               j+=1
     for i in range(1,N):
          count = 0
          j = 0
          while i+j < N:
               if table[i+j][j] == ch: count+=1
               else: count = 0
               if count == K: return true
               j+=1

def rotate():
     for i in range(0,N):
          pos = N-1
          for j in range(N-1,-1,-1):
               if temp[i][j] == 'B' or temp[i][j] == 'R':
                    table[pos][N-1-i] = temp[i][j]
                    pos -= 1

T = int(fin.readline())
for t in range(1,T+1):
     N,K = [int(x) for x in fin.readline().split(' ')]
     table = [['.' for j in range(0,N)]for i in range(0,N)]
     temp = [[]for i in range(0,N)]
     for i in range(0,N):
          temp[i] = fin.readline()
     rotate()
     ans = "Neither"
     if isJoin('R'): ans = "Red"
     if isJoin('B'):
          if ans == "Red": ans = "Both"
          else: ans = "Blue"
     print('Case #%d: %s' % (t,ans))
fin.close()
