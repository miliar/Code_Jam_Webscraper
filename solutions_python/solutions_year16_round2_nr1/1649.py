#!/usr/bin/env python
import sys

int_char = {
  0: 'ZERO',
  1: 'ONE',
  2: 'TWO',
  3: 'THREE',
  4: 'FOUR',
  5: 'FIVE',
  6: 'SIX',
  7: 'SEVEN',
  8: 'EIGHT',
  9: 'NINE'
}

def main(file):
  with open(file) as f:
    f.readline()
    cur_case = 1

    for line in f:
      line = line.rstrip('\n')
      letters_hash = {}
      current_number = 0
      phone = ''

      for char in line:
        if char in letters_hash:
          letters_hash[char] += 1
        else:
          letters_hash[char] = 1

      print 'Case #{}: {}'.format(
        cur_case,
        try_digit(dict(letters_hash), current_number)[1]
      )

      cur_case += 1

def try_digit(letters_hash, current_number):
  if hash_empty(letters_hash):
    return (True, '')

  for i in xrange(current_number, 10):
    result_current = try_make(dict(letters_hash), int_char[i])

    if result_current[0]:
      r1 = try_digit(dict(result_current[1]), i)
      if r1[0]:
        return (True, str(i) + r1[1])

      r2 = try_digit(dict(result_current[1]), i + 1)
      if r2[0]:
        return (True, str(i + 1) + r2[1])

  return (False, '')

def try_make(letters_hash, digit_char):
  for char in digit_char:
    if char in letters_hash and letters_hash[char] > 0:
      letters_hash[char] -= 1
    else:
      return (False, None)
  return (True, letters_hash)

def hash_empty(letters_hash):
  for key in letters_hash:
    if letters_hash[key] != 0:
      return False
  return True

if __name__ == '__main__':
  main(sys.argv[1])
