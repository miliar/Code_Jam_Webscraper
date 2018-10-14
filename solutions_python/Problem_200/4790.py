import os
dir_path = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dir_path, 'input.in')
outpath = os.path.join(dir_path, 'output.in')
def find_last_tidy_number(n):
  for i in range(n, 0,-1):
    if (sorted(str(i))) == list(str(i)):
      return i
  else:
    return 1

def main():
  result = []
  with open(filepath) as f:
    lines = f.readlines()[1:]
    for idx, line in enumerate(lines):
      result.append("Case #{}: {}".format(idx+1, find_last_tidy_number(int(line.strip()))));
      
  with open(outpath, 'w') as f:
    out = '\n'.join(result)
    f.write(out)

main()