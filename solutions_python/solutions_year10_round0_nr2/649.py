#!/usr/bin/python

import sys
import fractions

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    try:
      inputs = input.readline().rstrip().split()

      nb_dates = int(inputs[0])
      dates = inputs[1:]

      t = 0

      i = 0
      while i < nb_dates:
        dates[i] = int(dates[i])
        i += 1

      i = 0
      j = 0
      while i < nb_dates - 1:
        j = i + 1
        while j < nb_dates:
          t = fractions.gcd(t, abs(dates[i] - dates[j]))
          if t == 1:
            raise Exception
          j += 1
        i += 1

      if t == 1:
        answer = 0
      else:
        answer =  (t - (dates[0] % t)) % t

    except:
      answer = 0
    finally:
      output.write('Case #%d: %s\n' % (val,answer))

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
