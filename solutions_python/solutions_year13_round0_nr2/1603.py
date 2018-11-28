input = open('C:\Users\jbryan\Downloads\B-large.in').read()

output = ''

from numpy import fromstring, array, minimum, maximum
from pandas import Panel, DataFrame, Series

def str_to_Series(str):
  return Series(fromstring(str, dtype=int, sep=' '))

input = input.split('\n')
cases = int(input.pop(0))
for c in range(cases):
  n, m = tuple(str_to_Series(input.pop(0)))
  rows = input[:n]
  lawn_dict = dict(zip(range(n), map(str_to_Series, rows)))
  lawn_df = DataFrame.from_dict(lawn_dict, 'index')
  
  lawn_min = DataFrame(minimum.outer(lawn_df.max(axis=0), lawn_df.max(axis=1)))
  # ufunc .outer() has inconsistent transposition. elifs - don't want to re-transpose
  if lawn_min.shape != lawn_df.shape: lawn_min = lawn_min.transpose()
  elif any(lawn_min.max(axis=0) != lawn_df.max(axis=0)): lawn_min = lawn_min.transpose()
  elif any(lawn_min.max(axis=1) != lawn_df.max(axis=1)): lawn_min = lawn_min.transpose()
  
  lawn_pass = (lawn_min <= lawn_df).all().all()
  
  if lawn_pass: result = 'YES'
  else: result = 'NO'
  output = output + 'Case #{}: {}\n'.format(c+1, result)
  
  # # test stuff
  # if c > 30:
    # lawn_df[lawn_df==2] = 22
    # lawn_min[lawn_min==2] = 22
    # print lawn_df, '\n\n', lawn_min, '\n\n', lawn_pass, result
    # raw_input('Press enter')
  #
  input = input[n:]
#
output = output[:-1]
print output
with open('B-large.txt', 'w') as text_file:
  text_file.write(output)
#

