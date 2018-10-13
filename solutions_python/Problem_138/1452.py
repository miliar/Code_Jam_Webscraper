#!/usr/bin/env python3
import argparse, sys, os

def parse_and_run_input(inp):
  inp = inp.split('\n')
  num_tests = int(inp.pop(0))

  results = []
  for i in range(num_tests):
    base = i * 3

    size = int(inp[base])
    naomi = [float(val) for val in inp[base + 1].split(" ")]
    ken = [float(val) for val in inp[base + 2].split(" ")]
    deceit, regular = deceitful_war(size, naomi, ken)
    results.append("Case #%d: %d %d" % (i + 1, deceit, regular))

  return "\n".join(results)

def deceitful_war(size, naomi, ken):
  assert(size == len(naomi))
  assert(size == len(ken))

  size = len(naomi)
  naomi = sorted(naomi)[::-1]
  ken = sorted(ken)[::-1]
  ken2 = ken[:]

  deceit = 0
  for i in range(size):
    for j in range(size):
      if naomi[i] > ken[j]:
        ken[j] = float('Inf')
        deceit += 1
        break

  regular = 0
  for i in range(size):
    j = size - 1;
    while j >= 0:
      if ken2[j] >= naomi[i]:
        ken2[j] = -float('Inf')
        break;
      j -= 1
    if j == -1:
      regular += 1

  return deceit, regular

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
    verification_file = "%s.verify" % filename

    with open(verification_file) as vf:
      expected_results = vf.read().strip()
      if (results == expected_results):
        print('Results verified!')
      else:
        print('Expected:\n' + expected_results)
        print('Got:\n' + results)
  else:
    args.outfile.write(results)
