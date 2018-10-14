#!/usr/bin/python
import fractions

num_tests = int(raw_input())

def solve(p, q): 
  gcd = fractions.gcd(p, q)
  if gcd != 0: 
      p /= gcd
      q /= gcd
  if p == 1: 
    return power(q)
  if 2*p < q: 
    return solve(p-1, q/2) + 1
  else: 
    return 1

def power(num): 
  pow = 0
  while num > 1: 
    num /= 2
    pow += 1
  return pow
    
if __name__ == '__main__': 
  for test_num in range(num_tests): 
    p, q = raw_input().strip().split('/')
    p = int(p)
    q = int(q)
    result = 'impossible'
    gcd = fractions.gcd(p, q)
    if gcd != 0: 
      p /= gcd
      q /= gcd
      if bin(q)[2:].count('1') == 1: 
        result = solve(p, q)
        if result > 40: 
          result = 'impossible'
    print "Case #%d: %s" % (test_num+1, str(result))
