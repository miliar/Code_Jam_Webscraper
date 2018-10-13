import sys

def test(input_file):
  with open(input_file) as f:
    lines = f.readlines()
    n = int(lines[0].strip())

    for x in xrange(1, n+1):
      max_shyness, shyness_levels = lines[x].strip().split()
      cheering, friends = 0, 0
      for level, num_people in enumerate(shyness_levels):
        if num_people > 0 and cheering < level:
          new_friends = (level - cheering)
          friends += new_friends
          cheering += new_friends
        cheering += int(num_people)
      print "Case #{x}: {f}".format(x=x, f=friends)

test(sys.argv[1])