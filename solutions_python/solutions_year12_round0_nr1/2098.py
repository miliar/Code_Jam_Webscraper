"""Speaking in Tongues."""

import sys

LETTER_MAP = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q'
}

def main(argv=None):
  if not argv:
    argv = sys.argv

  input_file = open(argv[1])
  filename, _, _ = argv[1].partition('.')
  lines = [line.strip('\n') for line in input_file.readlines()]

  output_file = open('%s.out' % filename, 'w')

  num_cases = int(lines.pop(0))

  for n in xrange(0, num_cases):
    chars = list(lines.pop(0))
    translation = ''
    for c in chars:
      translation += LETTER_MAP.get(c, c)
    output_file.write('Case #%d: %s\n' % (n+1, translation))

  output_file.close()


if __name__ == '__main__':
  sys.exit(main())
