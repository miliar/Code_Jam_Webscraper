#!/usr/bin/python
import os, sys

def usage():
  print "Usage: standing_ovation.py filename"

def main():
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)

  filename = os.path.abspath(sys.argv[1])
  with open(filename) as input_file:
    data = input_file.read()
  input_lines = data.split("\n")
  for input_num, input_line in enumerate(input_lines[1:]):
    if len(input_line.replace(" ", "")) == 0:
      continue
    max_shyness = input_line.split()[0]
    audience_shyness = input_line.split()[1]
    num_friends = 0
    total_num_standing = 0
    for i in range(len(audience_shyness)):
      new_standups = 0
      if total_num_standing < i:
        new_standups = i - total_num_standing
        num_friends += new_standups
      new_standups += int(audience_shyness[i])
      total_num_standing += new_standups
    print "Case #%d: %d" % (input_num + 1, num_friends)



if __name__ == "__main__": 
  main()
