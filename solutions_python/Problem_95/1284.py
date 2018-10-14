#!/usr/bin/python2.6

# Standard libs
import string
import sys

GOOGLERESE_MAPPINGS = {
  "a" : "y",
  "b" : "h",
  "c" : "e",
  "d" : "s",
  "e" : "o",
  "f" : "c",
  "g" : "v",
  "h" : "x",
  "i" : "d",
  "j" : "u",
  "k" : "i",
  "l" : "g",
  "m" : "l",
  "n" : "b",
  "o" : "k",
  "p" : "r",
  "q" : "z",
  "r" : "t",
  "s" : "n",
  "t" : "w",
  "u" : "j",
  "v" : "p",
  "w" : "f",
  "x" : "m",
  "y" : "a",
  "z" : "q"
}

def translate_googlerese_char(char):
    if char not in string.letters:
        return char

    if char in GOOGLERESE_MAPPINGS:
        return GOOGLERESE_MAPPINGS[char]

    return "?"

def process_line(input_line):
    return "".join(map(translate_googlerese_char, list(input_line.lower())))

def main(argv):
    if len(argv) != 2:
        print "Usage: python %s INPUT_FILE" % (sys.argv[0])
        return 1

    input_filepath = argv[1]

    with open(input_filepath, "r") as input_file:
        print "\n".join([
            "Case #%d: %s" % (i + 1, process_line(line.strip()))
            for i, line
            in enumerate(input_file.readlines()[1:])
        ])

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

