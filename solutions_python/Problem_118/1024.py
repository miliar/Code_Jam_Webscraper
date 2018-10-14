test_cases = int(raw_input())

def solve(n):
  start , end = map(int , raw_input().split())
  def is_palindrome(n):
    s = str(n)
    l = len(s)
    return all(s[i] == s[l-1-i] for i in xrange(l))
  def is_square(n):
    return int(math.sqrt(n) ** 2) == n
  count=0
  current_sq = 1
  current = 1
  while current_sq < start:
    current_sq = current_sq + current + (current + 1)
    current +=1
  while current_sq <= end:
    if is_palindrome(current) and is_palindrome(current_sq):
      count +=1
    current_sq = current_sq + current + (current + 1)
    current +=1
  print "Case #{}: {}".format(n,count)
    
for i in xrange(test_cases):
  solve(i+1)