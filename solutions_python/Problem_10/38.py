#!/usr/bin/env python
#
# .py - 
#
# Copyright 2008 (C) Mansour Behabadi
#
# NOTE: this is the solution to code.jam contest problem:
#



# main program
if __name__ == '__main__':
   testsCount = int(raw_input())
   # process each test
   for cur_test in xrange(testsCount):
      max_letter_per_key, keys_count, letters_count = \
         [int(i) for i in raw_input().split(' ')]
      letter_freqs = [int(i) for i in raw_input().split(' ')]
      letter_freqs = [(i, letter_freqs[i]) for i in xrange(len(letter_freqs))]
      letter_freqs.sort(cmp=(lambda x, y: x[1].__cmp__(y[1])), reverse=True)
      key_letters = [0] * keys_count
      i = 0
      total_presses = 0
      for letter, freq in letter_freqs:
         key_letters[i] += 1
         total_presses += key_letters[i] * freq
         i = (i + 1) % len(key_letters)
      print "Case #%d: %d" % (cur_test + 1, total_presses)
