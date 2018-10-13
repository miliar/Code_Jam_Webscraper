#! /usr/bin/python
import sys
import pprint
PP = pprint.PrettyPrinter(indent=4).pprint

def tail_call_optimized(g):
  def function(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise Exception(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except Exception as e:
          args = e.args
          kwargs = e.kwargs
  return function

#@tail_call_optimized

def get_time(D, horses, index):
    Dk = horses[index][0]
    Sk = horses[index][1]
    # print "D = {}, {} ..".format(D, horses[index])
    # print "time = {}".format(float(D-Dk)/Sk)
    if index == 0:
        # print "    time = {:.6f}".format((D - Dk)/Sk)
        return (D - Dk)/Sk
    tn_minus_1 = get_time(D, horses, index - 1)
    tn_prime = (D - Dk)/Sk
    # print "tn-1 = {}, t`={}".format(tn_minus_1, float(tn_prime))
    if tn_prime > tn_minus_1:
        # print "Dk[{}] is sloooow".format(index)
        return tn_prime
    else:
        # print "Tk[{}] = {}".format(index, tn_minus_1 + (D - Sk * tn_minus_1)/Sk)
        return tn_minus_1

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        line = (lines.pop(0)).rstrip()
        D, N = [int(x) for x in line.split(' ')]
        D = float(D)
        horses = []
        while N > 0:
            N -= 1
            line = (lines.pop(0)).rstrip()
            ki, si = [int(x) for x in line.split(' ')]
            horses.append((ki, si))
        t = get_time(D, horses, len(horses)-1)
        print "Case #{}: {:.6f}".format(testcase, D/t)
        testcase += 1

if __name__ == '__main__':
    main()
