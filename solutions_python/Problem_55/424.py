#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    inputs = input.readline().rstrip().split()

    times = int(inputs[0])
    max_ppl = int(inputs[1])
    queue_size = int(inputs[2])

    queue = input.readline().rstrip().split()

    for x in range(queue_size):
      queue[x] = int(queue[x])

    ppl_cnt = 0
    for x in queue:
      ppl_cnt += x

    if (ppl_cnt <= max_ppl):
      money = ppl_cnt*times
      output.write('Case #%d: %s\n' % (val,money))
      continue

    ind = 0
    ppl = 0
    money = 0

    for x in range(times):
      ppl = 0
      while (ppl + queue[ind] <= max_ppl and ppl != ppl_cnt):
        ppl += queue[ind]
        ind += 1
        if ind == queue_size:
          ind = 0

      money += ppl

    output.write('Case #%d: %s\n' % (val,money))

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
