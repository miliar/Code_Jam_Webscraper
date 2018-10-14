def flip(pancakes, width):
    flips = 0
    for i in xrange(len(pancakes)-(width-1)):
        if pancakes[i] == "-":
            flips += 1
            pancakes[i] = "+"
            for pancake in xrange(i+1, i+width):
                if pancakes[pancake] == "+":
                    pancakes[pancake] = "-"
                else:
                    pancakes[pancake] = "+"
    success = True
    for i in xrange(1, width):
        if pancakes[-i] == "-":
            success = False
    return flips if success else "IMPOSSIBLE"

t = raw_input()
for i in xrange(1, int(t) + 1):
  case = raw_input().split(" ")
  pancakes, width = list(case[0]), int(case[1])
  print "Case #{}: {}".format(i, flip(pancakes, width))