import math
import sys

def get_ints(infile):
  return [int(x) for x in infile.readline().strip().split()]


def get_int(infile):
  return int(infile.readline().strip())


def read_case(infile):
  return infile.readline().strip()


def solve_case(data):
  chars = {}
  curr_max = 0
  for (index, char) in enumerate(data):
    if char not in chars:
      chars[char] = curr_max
      curr_max += 1
  
  char_1 = None
  char_0 = None
  for char in chars:
    if chars[char] == 0:
      char_0 = char
    if chars[char] == 1:
      char_1 = char
  
  chars[char_0] = 1
  chars[char_1] = 0
  base = len(chars.keys())
  
  val = 0
  for (i, char) in enumerate(data):
    val += math.pow(base, len(data)-i-1)*chars[char]
  return int(val)
  
  
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