import math
def palindrome(n):
  s = str(n)
  return s == s[::-1]

fairsquare = [False] * 1001
arr = [0] * 1001
arr[0] = 0
for i in range(1, int(math.sqrt(1001))+1):
  if palindrome(i) and palindrome(i*i):
    fairsquare[i*i]=True

for i in range(1,1001):
  arr[i] = arr[i-1]
  if fairsquare[i]:
    arr[i] += 1

cases = raw_input()
for i in range(1,int(cases)+1):
  [a,b] = raw_input().split(" ")
  print "Case #{0}: {1}".format(i, arr[int(b)] - arr[int(a)-1])
