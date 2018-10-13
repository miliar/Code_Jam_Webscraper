from itertools import *

filename = 'A-large'

def find_min_flips(pancakes, k) :
  if k < 1 :
    return 'IMPOSSIBLE'
  num_flips = 0
  while True :
    pancakes = list(dropwhile(lambda x: x, pancakes))
    if not pancakes : break
    elif len(pancakes) < k : return 'IMPOSSIBLE'
    pancakes = chain(map(lambda x: not x, pancakes[:k]), pancakes[k:])
    num_flips += 1
  return str(num_flips)

def find_answer(line) :
  params = line.split()
  pancakes = map(lambda c: c == '+', params[0])
  return find_min_flips(pancakes, int(params[1]))

with open(filename + '.out.txt', 'w') as output_file :
  with open(filename + '.in.txt', 'r') as input_file :
    n = int(input_file.readline())
    for case_number in range(1,n+1) :
      answer = find_answer(input_file.readline())
      output_file.write('Case #' + str(case_number) + ': ' + answer + '\n')
