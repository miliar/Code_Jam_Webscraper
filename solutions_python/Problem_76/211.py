import sys
import itertools

filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
  
def get_lines():
  f_in = open(filename)
  lines = f_in.readlines()
  lines = [line.strip() for line in lines]
  return lines[1:]

def rest_of(values, combo):
  other_combo = values[:]
  for c in combo:
    other_combo.remove(c)
  return other_combo
  
def xor(a,b):
  return a ^ b

def patrick(iterable):
  return reduce(xor, iterable, 0)

def solve(line):
  tokens = [int(x) for x in line.split(' ')]
  solution = -1

  values = tokens
  for r in range(1, len(values) + 1):
    for combo in itertools.combinations(values, r):
      rest = rest_of(values, combo)
      a, b = (patrick(combo), patrick(rest))
      if a == b:
        if sum(rest) > solution:
          solution = sum(rest)
      
  solution = 'NO' if solution < 0 else solution
  return solution

def main():
  lines = get_lines()
  new_lines = []
  for i, line in enumerate(lines):
    if i%2 == 1:
      new_lines.append(line)
  for (i, line) in enumerate(new_lines):
    solution = solve(line)
    print "Case #%s: %s" % (i+1, solution)

if __name__ == '__main__': main()
