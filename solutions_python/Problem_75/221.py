import sys
filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
  
def get_lines():
  f_in = open(filename)
  lines = f_in.readlines()
  lines = [line.strip() for line in lines]
  return lines[1:]

def combine(a, b, combinations):
  pair = set([a, b])
  for c in combinations:
    if pair == c[0]:
      return c[1]
  return None

def is_opposed(element, elements, oppositions):
  for e in set(elements):
    pair = set([element, e])
    if pair in oppositions:
      return True
  return False
  
def simplify(element_list, combinations, oppositions):
  if len(element_list) < 2:
    return element_list
  combined = combine(element_list[-2], element_list[-1], combinations)
  if combined:
    element_list = element_list[:-2] + [combined]
    return simplify(element_list, combinations, oppositions)
  if is_opposed(element_list[-1], element_list[:-1], oppositions):
    return []
  return element_list

def resolve(combinations, oppositions, invocations):
  element_list = []
  for invoked in invocations:
    element_list.append(invoked)
    element_list = simplify(element_list, combinations, oppositions)
  return element_list

def solve(line):
  tokens = line.split(' ')
  C = int(tokens[0])
  c_s = tokens[1:(1+C)]
  D = int(tokens[1+C])
  d_s = tokens[1+C+1:(1+C+1+D)]
  n_s = tokens[-1]
  combinations = [(set([c[0], c[1]]), c[-1]) for c in c_s]
  oppositions = [set([d[0],d[-1]]) for d in d_s]
  invocations = [c for c in n_s]
  return resolve(combinations, oppositions, invocations)

def main():
  lines = get_lines()
  for (i, line) in enumerate(lines):
    elements = solve(line)
    print "Case #%s: %s" % (i+1, '[' + ', '.join(elements) + ']')

if __name__ == '__main__': main()
