#!/usr/bin/env python3

def find_last_tidy_number(N):
  untidy = where_is_number_untidy(N)
  while untidy:
#    print("where is {} untidy? -> {}".format(N,untidy))
    N = make_tidy(N,untidy)
    untidy = where_is_number_untidy(N)
  return N

def where_is_number_untidy(x):
  x=str(x)
  for i in range(1,len(x)):
    if int(x[i])<int(x[i-1]):
      return i
  return 0

def make_tidy(x,untidy):
  x=list(str(x))
  x[untidy-1] = str(int(x[untidy-1])-1)
  for i in range(untidy,len(x)):
    x[i] = '9'
  return int(''.join(x))

T = int(input())
for i in range(1,T+1):
  N = int(input())
  y = find_last_tidy_number(N)
  print('Case #{}: {}'.format(i,y))

