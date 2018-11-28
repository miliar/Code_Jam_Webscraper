import sys

char_map = {
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
def translate(sentence, case_num):
  eng_sentence = ''
  for char in sentence:
    if char.isalpha():
      eng_sentence += char_map[char]
    elif char != '\n':
      eng_sentence += char
  print 'Case #' + repr(case_num) + ': ' + eng_sentence

if __name__ == '__main__':
  filename = sys.argv[1]
  infile = open(filename, 'r')

  cases = int(infile.readline())

  for i in xrange(1, cases + 1):
   sentence = infile.readline()
   translate(sentence, i)
