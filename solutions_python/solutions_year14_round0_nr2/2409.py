from codejam import *

def ff():
  c, f, x = read_float_list()
  r = 2
  t0 = 0
  t_est = x/r
  while True:
    t0 += c/r
    r += f
    t2 = x/r
    #print t_est, t0, t2, r
    if t_est < t0 + t2:
      return t_est
    t_est = t0+t2


main(ff)
