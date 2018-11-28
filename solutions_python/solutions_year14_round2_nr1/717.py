# cd C:/Dropbox/Joe/google_code_jam
filename = '2014-1B-A-small-attempt2'
input = open('C:\\Dropbox\\Joe\\google_code_jam\\{}.in'.format(filename)).read()
input = input.split('\n')
n_cases = int(input[0])
output = ''

from numpy import fromstring, array, minimum, maximum, floor
from pandas import Panel, DataFrame, Series
from datetime import datetime, timedelta
from scipy.stats.mstats import mode
prgm_start = datetime.now()

def str_to_Series(string):
  return Series(string.split(' '))

def str_to_int_Series(str):
  return Series(fromstring(str, dtype=int, sep=' '))
  
def str_to_bool_array(string):
  bool_array = Series(False, index=range(len(string)))
  for item in range(len(string)):
    bool_array[item] = bool(int(string[item]))
  return bool_array

def reverse_Series(s):
  return Series(array(s)[::-1], index=s.index)
  
def reduce_string(s):
  min_string = ''
  letter_count = []
  for char in s:
    if (len(min_string) > 0) and (char == min_string[-1]):
      letter_count[-1] += 1
    else:
      min_string += char
      letter_count.append(1)
  #
  return min_string, letter_count

def df_mode(df):
  f = lambda x: mode(x, axis=0)[0]
  return df.apply(f)

total_strings = 0
for c in range(n_cases):
  string_count = int(input[total_strings + c + 1])
  string_list = []
  min_string_list = []
  letter_count_list = []
  for s in range(string_count):
    new_string = input[total_strings + c + 1 + s + 1]
    min_string, letter_count = reduce_string(new_string)
    string_list.append(new_string)
    min_string_list.append(min_string)
    letter_count_list.append(letter_count)
  #
  if len(set(min_string_list)) == 1:
    df = DataFrame(letter_count_list)
    mode_df = df_mode(df)
    delta = (df - mode_df).abs()
    answer = int(delta.sum().sum())
  else:
    answer = 'Fegla Won'
  #
    
  total_strings = total_strings + string_count
  
  result = 'Case #{}: {}'.format(c+1, answer)
  print datetime.now(), '   ', result
  output = output + result + '\n'
#
x = (datetime.now() - prgm_start).total_seconds()
print 'Code run time = {:02.0f}:{:02.0f}:{:06.3f}'.format(floor(x/3600), floor((x%3600)/60), x%60)
with open('{}.txt'.format(filename), 'w') as text_file: text_file.write(output[:-1]) # strip last blank line