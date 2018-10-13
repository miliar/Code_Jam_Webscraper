import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

def follow(m, i, d):
   i += d
   while m[i] == '.':
      i += d
   return m[i]

def solve(m, C):
   res = 0
   for i, c in enumerate(m):
      if c != '.' and c!= '#':
         d = {'v':C, '>':1, '<':-1, '^':-C}[c]
         #print(i, follow(m,i,d))
         if follow(m, i, d) == '#':
            if any(follow(m,i,d2)!='#' for d2 in (C,-C,1,-1)):
               res += 1
            else:
               return -1
   return res

T, = read()
for testCase in range(T):
   R, C = read()
   m = '#'*(C+2)+''.join('#'+sys.stdin.readline().strip()+'#' for _ in range(R))+'#'*(C+2)
   #print(m)
   res = solve(m, C+2)
   if res == -1:
      res = 'IMPOSSIBLE'
   print('Case #{}: {}'.format(testCase+1, res))

