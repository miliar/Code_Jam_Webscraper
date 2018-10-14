import fileinput

def build_farm(c, f, x, cps):
  time_to_win = x / cps
  time_to_build_and_win = c / cps + x / (f+cps)
  return time_to_win > time_to_build_and_win, time_to_win

def main():

  text_input = fileinput.input()

  #num of test cases
  num = text_input.readline()

  for i in range(int(num)):

    #input for 1 case
    case_input = [float(x) for x in text_input.readline().rstrip().split(" ")]

    #c is farm price, f is extra cps per farm, x is goal
    c, f, x = case_input

    #cookies per second
    cps = 2.
    total_time = 0.

    # yeah.. true loop, whatever
    while True:
      build, time = build_farm(c, f, x, cps)
      if build:
        total_time += c / cps
        cps += f
      else:
        #time to get all cookies is reached
        total_time += time
        break

    print ("Case #{0}: {1:.7f}".format(i+1, total_time))

if __name__ == "__main__":
  main()
