import itertools
def complement(sublist, master):
  sublist = list(sublist)
  result = []
  for e in master:
    if e in sublist:
      sublist.remove(e)
    else:
      result.append(e)
  return result

def hog_candy(candy_values):
  def xorsum(somelist):
    return reduce(lambda x,y: x ^ y, somelist, 0)
  value = 0
  for size in xrange(1,len(candy_values)):
    possible_piles = itertools.combinations(candy_values, size)
    values = [max(sum(p), sum(complement(p, candy_values))) for p in possible_piles if xorsum(p) == xorsum(complement(p, candy_values))]
    if values:
      value = max(max(values), value)
  if value > 0:
    return value
  else:
    return "NO"

def main():
  infile = open("candy3.in", "r", True)
  inputs = infile.readlines()
  tests = int(inputs[0].strip())
  for i in xrange(tests):
    candies = int(inputs[(2*i)+1].strip())
    candy_values = [int(a) for a in inputs[(2*i)+2].split()]
    result = hog_candy(candy_values)
    print "Case #%s: %s" % (i+1, result)

if __name__ == '__main__':
  main()
