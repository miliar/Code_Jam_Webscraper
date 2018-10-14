input = open('C:\Users\jbryan\Downloads\C-small-attempt1.in').read()
input = input.split('\n')
case_count = int(input.pop(0))

output = ''

from numpy import fromstring, array, minimum, maximum, sqrt, arange, square
from pandas import Panel, DataFrame, Series

def str_to_Series(str):
  return Series(fromstring(str, dtype=int, sep=' '))
  
def int_palendrome(x):
  return str(x) == str(x)[::-1]

case_dict = dict(zip(range(case_count), map(str_to_Series, input)))
case_df = DataFrame.from_dict(case_dict, 'index')
max_val = case_df.max().max()
min_val = case_df.min().min()
sqrts = range(int(sqrt(min_val)), int(sqrt(max_val)) + 1)
sqrts = Series(sqrts, index=sqrts)
sqrt_pal = sqrts.apply(int_palendrome)
sqrt_pal = sqrts[sqrt_pal]
sqrs = sqrt_pal.apply(square)
sqr_pal = sqrs.apply(int_palendrome)
sqr_pal = sqrs[sqr_pal]

for c in case_df.index:
  a = case_df.ix[c, 0]
  b = case_df.ix[c, 1]
  fair = (sqr_pal >= a) & (sqr_pal <= b)
  output = output + 'Case #{}: {}\n'.format(c+1, fair.sum())
#
output = output[:-1]
print output
with open('C:\Dropbox\Joe\google_code_jam\C-small.txt', 'w') as text_file:
  text_file.write(output)
#

