import sys

def is_consenants(ss):
  for letter in ss:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
      return False
  return True

def count_substrings(word, n):
  count = 0
  last_ss = -1
  for i in range(len(word) - n + 1):
    if is_consenants(word[i:i+n]):
      if last_ss == -1:
        count += (i + 1) * (len(word) + - n - i + 1)
        last_ss = i + 1
      else:
        count += (i + 1 - last_ss) * (len(word)  - n - i + 1)
        last_ss = i + 1
  return count

num_cases = int(raw_input())
for casenum in range(1, num_cases+1):
  count = 0
  word, n = raw_input().split()
  n = int(n)
  num_ss = count_substrings(word, n)
  print "Case #" + str(casenum) +  ": " + str(num_ss) 
      
