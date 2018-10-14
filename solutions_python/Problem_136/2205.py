import sys

def compute(C, F, X):
  seconds = 0.0
  rate = 2.0

  while True:
    # Number of seconds to get a farm and then there.
    to_farm = C / rate + X / (rate + F)
    # Number of seconds to just go directly there.
    to_direct = X / rate

    if to_farm < to_direct:
      seconds += C / rate
      rate += F
    else:
      seconds += X / rate
      break

  return seconds

if __name__ == '__main__':
  f = open(sys.argv[1], 'r')
  out = open("B-large.out", 'w')
  num_cases = int(f.readline())
  
  for case_num in range(1, num_cases + 1):
    line = f.readline()
    [C, F, X] = [float(x) for x in line.split()]

    output = "Case #" + str(case_num) + ": " + str(compute(C, F, X))
    print output
    out.write(output + "\n")
  
  out.close()