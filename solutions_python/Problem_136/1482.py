#!/usr/bin/env python3
import argparse, sys, os

def parse_and_run_input(inp):
  inp = inp.split('\n')
  num_tests = int(inp.pop(0))

  results = []
  for i in range(num_tests):
    c, f, x = [float(val) for val in inp[i].split(" ")]
    result = cookie_clicker_alpha(c, f, x)
    # TODO: print to 6 decimal places
    results.append("Case #%d: %f" % (i + 1, result))

  return "\n".join(results)

def cookie_clicker_alpha(c, f, x):
  total_seconds = 0.0
  cookies_per_second = 2.0

  while True:
    seconds_to_win =  x / cookies_per_second

    seconds_to_next_factory = c / cookies_per_second
    seconds_to_win_with_next_factory = \
      seconds_to_next_factory + (x / (cookies_per_second + f))

    if seconds_to_win_with_next_factory < seconds_to_win:
      total_seconds += seconds_to_next_factory
      cookies_per_second += f
    else:
      total_seconds += seconds_to_win
      break

  return total_seconds

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
