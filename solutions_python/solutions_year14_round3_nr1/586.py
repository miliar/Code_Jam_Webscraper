import os
import fractions
import math
problem = '.'.join(os.path.basename(__file__).split('.')[:-1])
  
def main():
  inf = open(get_input_file())
  outf = open(problem + '.out', 'w')
  num_cases = int(inf.readline())
  problem_output = []
  for case_num in range(1, num_cases + 1):
    result = ''
    # per case stuff goes here
    # if only setting one variable, remember the comma after the variable name
    p, q = map(int, inf.readline().strip().split('/'))
    gcd = fractions.gcd(p, q)
    p /= gcd
    q /= gcd
    log = math.log(q, 2)
    if math.floor(log) != log:
      result = 'impossible'
    else:
      frac = fractions.Fraction(p, q)
      gen = 1
      while frac < fractions.Fraction(1, 2):
        frac *= 2
        gen += 1
      result = str(gen)
    # end per-case stuff
    problem_output.append('Case #' + str(case_num) + ': ' + result)
  outf.write('\n'.join(problem_output))
  print '\n'.join(problem_output)
  outf.close()
  inf.close()

def get_input_file():
  download_dir = os.path.expanduser('~/Downloads')
  last_updated = 0
  newest = ''
  example = '../examples/' + problem + '.exin'
  if os.path.exists(example):
    last_updated = os.path.getmtime(example)
  for fname in os.listdir(download_dir):
    if (fname.endswith('.in') and 
        fname.startswith(problem) and 
        os.path.getmtime(download_dir + '/' + fname) > last_updated):
      newest = fname
      last_updated = os.path.getmtime(download_dir + '/' + fname)
  if newest == '':
    return example
  else:
    return download_dir + '/' + newest

def fetch_spaced_types(inf, typ=int):
  return map(typ, inf.readline().strip().split(' '))

if __name__ == '__main__':
  main()
