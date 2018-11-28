#!/usr/bin/python

num_tests = int(raw_input())

def solve(strings): 
  if not any(strings): 
    return 0
  if not all(strings): 
    return float('inf')
    
  substrings = []
  string_counts = []
  match_char = strings[0][0]
  for x in strings: 
    count = 0
    while len(x) and x[0] == match_char:
      count += 1 
      x = x[1:]
    if not count: 
      return float('inf')
    substrings.append(x)
    string_counts.append(count)
  return find_min_changes(string_counts) + solve(substrings)

def find_min_changes(counts): 
  min_num = min(counts)
  max_num = max(counts)
  min_changes = float('inf')
  for i in range(min_num, max_num+1): 
    changes = 0
    for x in counts: 
      changes += abs(x-i)
    min_changes = min(min_changes, changes)
  return min_changes
    
if __name__ == '__main__': 
  for test_num in range(num_tests): 
    num_strings = int(raw_input())
    strings = []
    for i in xrange(num_strings): 
      strings.append(raw_input().strip())
    result = solve(strings)
    if result == float('inf'): 
      result = "Fegla Won"
    print "Case #%d: %s" % (test_num+1, str(result))
