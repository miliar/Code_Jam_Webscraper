"""Password Problem"""

import itertools
import sys

def product_wrapper(args):
  return itertools.product(*args)

def main(argv=None):
  if not argv:
    argv = sys.argv

  input_file = open(argv[1])
  lines = [line.strip('\n') for line in list(input_file.readlines())]

  filename = argv[1].partition('.')[0]

  output_file = open('%s.out' % filename, 'w')

  num_cases = int(lines.pop(0))

  for n in xrange(0, num_cases):
    num_typed, num_chars = [int(i) for i in lines.pop(0).split(' ')]
    prob_list = [float(i) for i in lines.pop(0).split(' ')]

    prob_args = []
    for p in prob_list:
      prob_args.append([p, 1 - p])

    prob_keys = []
    key_count_list = []
    for p_list in list(product_wrapper(prob_args)):
      prob = 1
      bool_list = []
      for i in xrange(0, num_typed):
        p = p_list[i]
        if p == prob_list[i]:
          bool_list.append(True)
        else:
          bool_list.append(False)
        prob *= p
      prob_keys.append(prob)

      key_counts = []
      for back in xrange(0, num_typed+1):
        if not back:
          test_list = bool_list
        else:
          test_list = bool_list[:(back*-1)]
        if False in test_list:
          keys = 2 * (back + num_chars + 1) - num_typed
        else:
          keys = 2 * back + num_chars - num_typed + 1
        key_counts.append(keys)
      key_enter = num_chars + 2
      key_counts.append(key_enter)
      key_count_list.append(key_counts)

    optimal = None
    for action in xrange(0, num_typed+2):
      expected = 0
      for x in xrange(0, len(prob_keys)):
        prob = prob_keys[x]
        key_counts = key_count_list[x]
        expected += prob * key_counts[action]
      if not optimal or expected < optimal:
        optimal = expected

    out_str = 'Case #%d: %f\n' % (n+1, optimal)
    output_file.write(out_str)

  output_file.close()


if __name__ == '__main__':
  sys.exit(main())
