# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

def cake(rows):
  prefix_rows = 0
  out = []
  for row in rows:
    stripped = row.translate(None, b'?')
    if not stripped:
      # our row is all ?s
      if out:
        # repeat the previous row
        out.append(out[-1])
      else:
        # We're in the first row, nothing to copy yet.
        prefix_rows += 1
        continue
    else:
      next_row_out = ''
      replace_char = stripped[0]
      for c in row:
        if not c == '?':
          replace_char = c
        next_row_out += replace_char
      out.append(next_row_out)
  out = (out[0:1] * prefix_rows) + out
  return out


if __name__ == '__main__':
  num_cases = int(raw_input())
  for case in range(num_cases):
    label = 'case #{}:'.format(case + 1)
    r, c = [int(x) for x in raw_input().split(' ')]
    rows = [raw_input() for row in range(r)]
    print(label)
    for output in cake(rows):
      print(output)
