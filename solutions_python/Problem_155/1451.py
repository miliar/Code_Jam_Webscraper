#!/usr/bin/env python

def main():
    f = open('standing_ovation_input.txt')

    line = f.readline()
    cases = int(line)

    of = open('standing_ovation_output.txt', 'w')
    for i in range(cases):
        res = "Case #%d: %s" % (i+1, test_case(f))
        print(res)
        of.write(res + "\n")
    of.close()
    f.close()

def test_case(ff):
  SMAX, STR = ff.readline().strip().split(' ')
  SMAX = int(SMAX)

  total_audience = 0
  initial_audience = 0
  for i in range(SMAX+1):
    c = int(STR[i])
    initial_audience += c
    if i > total_audience:
      total_audience =i#+= (i - total_audience) + 1
    total_audience += c

  return total_audience - initial_audience

main()
