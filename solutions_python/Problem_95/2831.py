import string
import sys
googleRese =  {
' ': ' ','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q':'z','z':'q'}

n = int(raw_input())

for i in range(1,n+1):
  line = raw_input()
  print 'Case #%d: '%i,
  for char in line:
    sys.stdout.write(googleRese[char]) 
  print '\n',
