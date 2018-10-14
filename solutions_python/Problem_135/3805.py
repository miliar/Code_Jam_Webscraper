from sys import stdin

def solve(a, b, c):
   # print a, b, c
   d = set(b[a[0]]) & set(c[a[1]])
   # print d
   size = len(d)
   if size == 0:
      return "Volunteer cheated!"
   elif size == 1:
      return d.pop()
   else:
      return "Bad magician!"

T = int(stdin.readline())
for i in range(T):
   a = [0, 0]
   a[0] = int(stdin.readline()) - 1
   b = [[], [], [], []]
   b[0] = [int(j) for j in stdin.readline().split()]
   b[1] = [int(j) for j in stdin.readline().split()]
   b[2] = [int(j) for j in stdin.readline().split()]
   b[3] = [int(j) for j in stdin.readline().split()]
   a[1] = int(stdin.readline()) - 1
   c = [[], [], [], []]
   c[0] = [int(j) for j in stdin.readline().split()]
   c[1] = [int(j) for j in stdin.readline().split()]
   c[2] = [int(j) for j in stdin.readline().split()]
   c[3] = [int(j) for j in stdin.readline().split()]
   print "Case #{}: {}".format(i+1, solve(a, b, c))