#!/usr/bin/env python3
import argparse, sys, os

def parse_and_run_input(inp):
  inp = inp.split('\n')
  num_tests = int(inp.pop(0))
  lines_per_test = 10
  parse_card_row = lambda r: [int(n) for n in r.strip().split(' ')]

  results = []
  for i in range(num_tests):
    base = i * lines_per_test

    row1 = int(inp[base])
    cards1 = list(map(parse_card_row, inp[base + 1: base + 5]))
    row2 = int(inp[base + 5])
    cards2 = list(map(parse_card_row, inp[base + 6: base + 10]))

    results.append("Case #%d: %s" % (i + 1, magic_trick(row1, cards1, row2, cards2)))

  return "\n".join(results)

def magic_trick(row1, cards1, row2, cards2):
  picked_cards_1 = set(cards1[row1 - 1])
  picked_cards_2 = set(cards2[row2 - 1])

  overlap = picked_cards_1.intersection(picked_cards_2)

  if (len(overlap) == 1):
    return str(overlap.pop())
  elif (len(overlap) == 0):
    return "Volunteer cheated!"
  else:
    return "Bad magician!"

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    'infile',
    nargs='?',
    type=argparse.FileType('r'),
    default=sys.stdin,
  )
  parser.add_argument(
    'outfile',
    nargs='?',
    type=argparse.FileType('w'),
    default=sys.stdout,
  )
  parser.add_argument('-v', '--verify', action='store_true')
  args = parser.parse_args()

  results = parse_and_run_input(args.infile.read())
  if (args.verify):
    filename = os.path.splitext(args.infile.name)[0]
    verification_file = "%s.out" % filename

    with open(verification_file) as vf:
      assert(results == vf.read().strip())
      print('Results verified!')

  args.outfile.write(results)
