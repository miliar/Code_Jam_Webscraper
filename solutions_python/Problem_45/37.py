import sys

def get_ints(infile):
  return [int(x) for x in infile.readline().strip().split()]


def get_int(infile):
  return int(infile.readline().strip())


def read_case(infile):
  data = {}
  data['p'],data['q'] = get_ints(infile)
  data['to_release'] = get_ints(infile)
  return data

def compute_min(p, q, to_release):
  if q == 1:
    return p-1
  
  if q == 0:
    return 0
  
  base_cost = p-1
  min_cost = None
  for i in range(q):
    left_side = compute_min(to_release[i]-1, i, to_release[:i])
    right_side = compute_min(p-to_release[i], q-i-1, [x-to_release[i] for x in to_release[i+1:]])
    if min_cost is None:
      min_cost = left_side + right_side + base_cost
    else:
      min_cost = min(left_side + right_side + base_cost, min_cost)
  return min_cost
    

def solve_case(data):
  return compute_min(data['p'], data['q'], data['to_release']) 


def print_solution(solution, outfile):
  outfile.write(' %d\n' % solution)


def main():
  if len(sys.argv) < 2:
    infile = sys.stdin
  else:
    infile = open(sys.argv[1], 'r')
    
  outfile = sys.stdout
  
  num_trials = get_int(infile)
  
  for case in range(num_trials):
    data = read_case(infile)
    solution = solve_case(data)
    outfile.write('Case #%d:' % (case+1))
    print_solution(solution, outfile)


if __name__ == '__main__':
  main()