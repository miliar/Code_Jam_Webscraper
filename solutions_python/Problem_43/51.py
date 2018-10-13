#!/usr/bin/env python
import sys
import copy


alphabet = ['0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
  global alphabet
  
  T = int(sys.stdin.readline().strip())
  for case in range(1, T + 1):
    
    symbols = dict()

    string = sys.stdin.readline().strip()

    letters = copy.copy(alphabet)

    chars = list(string)

    for i in range(len(chars)):
      if i == 0:
        symbols[chars[i]] = letters.pop(1)
      else:
        if chars[i] not in symbols:
          symbols[chars[i]] = letters.pop(0)
    
    new = ''
    for i in range(len(chars)):
      new += symbols[chars[i]]


    if len(symbols) == 1 and len(new) == 1:
      print 'Case #' + str(case) + ':', 1
    elif len(symbols) == 1:
      print 'Case #' + str(case) + ':', int(new, 2)
    else:
      print 'Case #' + str(case) + ':', int(new, len(symbols))


if __name__ == '__main__':
  main()
