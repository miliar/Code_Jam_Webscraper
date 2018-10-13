
#variation on bubblesort
def find_closest_tidy_num(num):
    splits = [int(x) for x in str(num)]

    sorted = False

    while not sorted:
        sorted = True
        for x in xrange(0, len(splits) - 1):
            if(splits[x] > splits[x + 1]):
                splits[x] =  splits[x] - 1
                sorted = False
                for y in xrange(x + 1, len(splits)):
                    splits[y] = 9

    return int(''.join(map(str, splits)))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  x = find_closest_tidy_num(n)
  print "Case #{}: {}".format(i, x)
