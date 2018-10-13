from collections import deque
def palindrome(no):
  return str(no) == str(no)[::-1]

cnt = 1
cache = {}
for i in range(0,1001):
  if palindrome(i) and palindrome(i*i):
    cache[i*i] = True

with open('input.in', 'r') as f:
  read_data = f.read()
  read_data = deque(read_data.split("\n"))
  
  N = read_data.popleft()
  while read_data:
    line = read_data.popleft()
    if not line:
      continue
    A = long(line.split(" ")[0])
    B = long(line.split(" ")[1])
    p = 0
    for i in range(A,B+1):
      if cache.get(i):
        p = p + 1
    print "Case #%d: %d" % (cnt, p)
    cnt = cnt + 1

    
