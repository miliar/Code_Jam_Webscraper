import codejam
import re
import pdb


class AlienLanguage(codejam.CodeJam):
  def main(self):
    filename = self.get_filename()
    input = open(filename, 'r')
    first_line = input.readline()
    first_line = first_line.split(' ')
    first_line = map(int, first_line)
    letters, dictionary_length, num_cases = first_line
    dictionary = self.get_dictionary(input, dictionary_length)
    output = open('output_' + filename, 'w')
    for i in xrange(1, num_cases + 1):
      case = input.readline()
      case = self.convert_to_regex(case)
      matches = 0
      for word in dictionary:
        if re.match(case, word) != None:
          matches += 1
      output.write('Case #%d: %d\n' % (i, matches))
    output.close()
    input.close()

  def get_dictionary(self, input, dictionary_length):
    dictionary = []
    for i in xrange(dictionary_length):
      word = input.readline()
      dictionary.append(word)
    return dictionary

  def convert_to_regex(self, word):
    word = word.replace('(','[')
    word = word.replace(')',']')
    word = word.replace(',','')
    return word



if __name__ == "__main__":
  reload(codejam)
  al = AlienLanguage()
  al.main()
