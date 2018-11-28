fp = open("large.in")  #input filename
fout = open("large_out.txt", "w") #output filename


def get_input():
    t = int(fp.readline())
    for i in xrange(t):
        n = int(fp.readline())
        array = map(int, fp.readline().split())
        yield n, array


# Sort an array in place and return the number of writes.
# From http://en.wikipedia.org/wiki/Cycle_sort
def cycleSort(array):
  writes = 0
 
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
 
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
 
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
 
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
 
    # Rotate the rest of the cycle.
    while pos != cycleStart:
 
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
 
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
 
  return writes

for i,j in enumerate(get_input(), 1):
    #print n
    n, array = j
    r = cycleSort(array) * 1.0
    print "Case #%s: %.6f" % (i, r)
    print >> fout, "Case #%s: %s" % (i, r)

fout.close()

