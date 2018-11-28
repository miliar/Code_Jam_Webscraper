#!/usr/bin/env python

import sys
import os

dict = {
   'y': 'a',
   'n': 'b',
   'f': 'c',
   'i': 'd',
   'c': 'e',
   'w': 'f',
   'l': 'g',
   'b': 'h',
   'k': 'i',
   'u': 'j',
   'o': 'k',
   'm': 'l',
   'x': 'm',
   's': 'n',
   'e': 'o',
   'v': 'p',
   'z': 'q',
   'p': 'r',
   'd': 's',
   'r': 't',
   'j': 'u',
   'g': 'v',
   't': 'w',
   'h': 'x',
   'a': 'y',
   'q': 'z',
   ' ': ' ',
}

def process_file(inp_file, out_file):
   curr_line = 1
   total_test = 0
   lines = open(inp_file)
   out = open(out_file, 'w+')
   for line in lines:
      if curr_line == 1:
         total_test = line
         curr_line += 1
      else:
         out_str = translate(line.rstrip('\n'))
         print >> out, 'Case #%s: %s' % (curr_line-1, out_str)
         curr_line += 1


def translate(str):
   output = '';
   for c in str:
     output = "%s%s" % (output,dict[c])
   return output

def main(argv):
   if len(argv) < 3:
      sys.stderr.write('Usage: %s <input_filename> <output_filename>\n' % argv[0])
      return 1

   if not os.path.exists(argv[1]):
      sys.stderr.write('ERROR: File %s was not found!\n' % argv[1])
      return 1
   
   process_file(argv[1], argv[2])

   return 0  

if __name__ == "__main__":
    sys.exit(main(sys.argv))
