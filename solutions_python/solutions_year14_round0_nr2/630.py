def solve(fname):
  output = open("output.txt", "w+")
  with open(fname, "r") as f:
    numCases = int(f.readline())

    # as long as the overall time decreases from the buying of one farm to
    # the next, keep on going; at the first increase, return the time
    for i in xrange(numCases):
      inp = f.readline().split(" ")

      # input values
      C, F, X = float(inp[0]), float(inp[1]), float(inp[2])

      # variables we need to keep track of
      # time => time elapsed thus far
      # shortest => last shortest time
      # prodCount => number of cookies we are producing per second
      # curr => curr shortest time
      time, shortest, prodCount, curr = 0.0, 0, 2, X/2

      while True:
        # buy a farm
        time += C / prodCount

        # change prod count
        prodCount += F

        # shortest = time it takes to get from 0 to X with new prodcount
        shortest = X / prodCount

        # if new shortest (shortest) is greater than old shortest (mx)
        # then break and return shortest
        if (shortest + time) > curr:
          output.write("Case #{}: {}\n".format(i+1, curr))
          break
        else:
          curr = time + shortest

solve("input.in")
