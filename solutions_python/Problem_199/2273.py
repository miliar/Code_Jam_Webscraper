import sys

def flip_character(c):
  if(c=='-'):
    return '+'
  else:
    return '-'

def fliped(text, start, K):
  return text[0:start] + ''.join(map(flip_character, text[start:start+K])) + text[start+K:]

def is_end(text):
  return all(map(lambda c: c=='+', text))

def solve(case_index, data, K):
  cache = {}

  curr = data
  count = 0
  for i in range(0, len(data)-K+1):
    if curr[i]=='-':
      curr = fliped(curr, i, K)
      count += 1
  
  if is_end(curr):
    print("Case #{}: {}".format(str(case_index), str(count)))
  else:
    print("Case #{}: {}".format(str(case_index), 'IMPOSSIBLE'))

if __name__=='__main__':
  test_count = int(input())
  test_cases = [(line.split(' ')[0], int(line.split(' ')[1])) for line in sys.stdin]

  for index, (data, k) in zip(range(1, test_count+1), test_cases):
    solve(index, data, k)

