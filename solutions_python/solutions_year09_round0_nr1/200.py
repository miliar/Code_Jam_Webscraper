import logging
import re

class AlienLanguage:

    def __init__(self,  word_length):
        self.word_length = word_length
        self.words = {}
        self.vocab = [ set() for i in range(word_length)]

    def add_word(self, word, words = None):
      if words == None:
        words = self.words
      self.vocab[self.word_length - len(word)].add(word[0])
      if len(word) == 1:
        words[word] = word
      else:
        if word[0] not in words:
          words[word[0]] = {}
        self.add_word(word[1:], words[word[0]])

    def count_words(self, pattern):
      logging.debug(pattern)
      sequence = []
      i = 0
      for m in re.finditer(r"\((\w+)\)|(\w)", pattern):
        letters = []
        group, letter = m.groups()
        if group == None:
          if letter in self.vocab[i]:
            letters = [letter]
        else:
          for c in group:
            if c in self.vocab[i]:
              letters.append(c)
        if len(letters) == 0:
          return 0
        sequence.append(letters)
        i += 1

      return self.count_sequence(sequence, self.words)

    def count_sequence(self, sequence, words):
      
      if words == None:
        words = self.words
      group = sequence[0]

      count = 0
      for letter in group:
        if letter in words:
          if len(sequence) == 1:
            count += 1
          else:
            count += self.count_sequence(sequence[1:], words[letter])

      return count

#logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":

  (L, D, N) = map(int, raw_input().split())
  lang = AlienLanguage(L)

  for i in range(D):
    lang.add_word(raw_input())

  logging.debug(lang.vocab)

  for i in range(N):
    print  'Case #' + str(i+1)  + ': ' + str(lang.count_words(raw_input()))

