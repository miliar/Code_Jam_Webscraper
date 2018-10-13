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

def read_line(i):
  return set([ read_ints() for x in range(4) ][i])



if __name__ == "__main__":
    T = read_int()
    for c in range(T):

        line1 = read_line(read_int() - 1)
        line2 = read_line(read_int() - 1)
        result = line1.intersection(line2)
        size = len(result)

        if size > 1:
          R = "Bad magician!"
        elif size == 1:
          R = result.pop()
        else:
          R = "Volunteer cheated!"

        print("Case #{}: {}".format(c+1,R))
