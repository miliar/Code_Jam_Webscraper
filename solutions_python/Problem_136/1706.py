#!/usr/bin/env python3

################################################################################

def read_int():
  return int(input())

def read_words():
  return input().split()

def read_ints():
  return map(int,read_words())

def read_floats():
  return map(float,read_words())

################################################################################

def solve(c,f,x):

  r = 2.0
  already_spent = 0.0
  est = x / r
  cn = 0

  while True:

    house_time = c / r
    nr = r + f
    nest = (x / nr) + already_spent + house_time
    
    if nest - est >= -1e-7:
      break
    
    r = nr
    already_spent += house_time
    est = nest
    cn += 1

  return est



if __name__ == "__main__":
    T = read_int()
    for c in range(T):
        [C, F, X] = read_floats()
        R = solve(C,F,X)
        print("Case #{}: {:.7f}".format(c+1,R))
