#import locale
#locale.setlocale(locale.LC_ALL, "")

# http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":

  #input = [26000000, 11000000, 6000000]
  #input = [1, 10, 11]
  #input = [800000000000000000001, 900000000000000000001]

  count = int(raw_input())
  for i in range(count):
    input = [int(s) for s in raw_input().split(" ")[1:]]
    #print 'input:', [locale.format('%d', x, True) for x in input]
    input.sort(reverse = True)
    first = input[0]
    #print 'first:', locale.format('%d', first, True)
    events = [ first - x for x in input[1:] ]
    #print 'events:', [locale.format('%d', x, True) for x in events]
    ggcd = reduce(gcd, events)
    #print 'ggcd:',locale.format('%d', ggcd, True)

    solution = -first % ggcd

    #print "solution:",locale.format('%d', solution, True)

    print 'Case #' + str(i+1)  + ': ' + str(solution)



