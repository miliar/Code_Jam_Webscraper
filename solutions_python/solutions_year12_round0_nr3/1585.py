"""Recycled Numbers."""

import sys

def main(argv=None):
  if not argv:
    argv = sys.argv

  input_file = open(argv[1])
  lines = [line.strip('\n') for line in input_file.readlines()]

  filename = argv[1].partition('.')[0]

  output_file = open('%s.out' % filename, 'w')

  num_cases = int(lines.pop(0))

  for n in xrange(0, num_cases):
    A, B = lines.pop(0).split()

    if len(A) == 1:
      output_file.write('Case #%d: 0\n' % (n+1))
      continue

    recycled_pairs = []
    A_int = int(A)
    B_int = int(B)
    for base_num in xrange(A_int, B_int+1):
      base_str = str(base_num)
      for i in xrange(1, len(base_str)):
        candidate = base_str[i:] + base_str[0:i]
        num_str = candidate.lstrip('0')
        num = int(num_str)
        if len(base_str) == len(num_str) and base_num != num:
          if base_num < num:
            key = base_num
            val = num
          else:
            key = num
            val = base_num
          if ((key, val) not in recycled_pairs
              and key >= A_int and val <= B_int):
            recycled_pairs.append((key, val))

    output_file.write('Case #%d: %s\n' % (n+1, len(recycled_pairs)))

  output_file.close()


if __name__ == '__main__':
  sys.exit(main())
