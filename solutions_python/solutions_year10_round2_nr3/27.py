#!/usr/bin/python

import sys
import gmpy

import results
#results = dict()

def nbcomb(n, k):
  if k == 1 or k == n-1:
    return 1

  if (n, k) in results.results:
    return results.results[(n, k)]

  answer = 0
  x = 1
  while x < k:
    val = nbcomb(k, x)
    answer += gmpy.comb(n-k-1, k-x-1)*val
    x += 1

  answer = int(answer)%100003

  results.results[(n, k)] = answer

  return answer

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    n = int(input.readline().rstrip())
    answer = 0

    print("test", val)
    k = 1
    while k < n:
      answer += nbcomb(n, k)
      k += 1

#    print results

    output.write('Case #%d: %s\n' % (val,answer%100003))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Need file as argument"
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
