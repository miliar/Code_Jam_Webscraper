import logging

class SubstringCounter:

  def __init__(self,  needle, haystack):
    self.needle = needle
    self.haystack = haystack
    self.cache = {}

  def count(self, needle = None, start = 0):

    # init
    if needle == None:
      needle = self.needle

    logging.debug('|' + needle + '|' + self.haystack[start:] + '|')

    # check cache
    if (needle, start) in self.cache:
      logging.debug('HIT ' + str((needle, start)) + ' ' + str(self.cache[(needle, start)]))
      return self.cache[(needle, start)]

    # check if needle does not fit in haystack
    if len(needle) > len(self.haystack) - start:
      logging.debug('X ' + str((needle, start)))
      self.cache[(needle, start)] = 0
      return 0


    # no match on first letter? let's break or advance
    if needle[0] != self.haystack[start]:
      if start == len(self.haystack) - 1:
        self.cache[(needle, start)] = 0
        return 0
      else:
        result = self.count(needle, start + 1)
        self.cache[(needle, start)] = result
        return result

    # count number of repeats for this letter
    repeats = 0
    while len(self.haystack) > start + repeats and needle[0] == self.haystack[start + repeats]:
      repeats += 1
    if len(needle) == 1:
      result =  repeats + self.count(needle, start + repeats)
      self.cache[(needle, start)] = result
      return result

    result = repeats * self.count(needle[1:], start + repeats)  + self.count(needle, start + repeats)
    self.cache[(needle, start)] = result
    return result
    

if __name__ == "__main__":

#  logging.basicConfig(level=logging.DEBUG)

  needle = "welcome to code jam"
  N = int(raw_input())

  for i in range(N):
    c = SubstringCounter(needle, raw_input())
    print  'Case #' + str(i+1)  + ': ' + "%04d" % (c.count() % 10000)

