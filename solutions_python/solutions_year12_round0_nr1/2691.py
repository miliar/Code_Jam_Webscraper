#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

dic = {
        'y':'a',
        'n':'b',
        'f':'c',
        'i':'d',
        'c':'e',
        'w':'f',
        'l':'g',
        'b':'h',
        'k':'i',
        'u':'j',
        'o':'k',
        'm':'l',
        'x':'m',
        's':'n',
        'e':'o',
        'v':'p',
        'z':'q',
        'p':'r',
        'd':'s',
        'r':'t',
        'j':'u',
        'g':'v',
        't':'w',
        'h':'x',
        'a':'y',
        'q':'z',
        ' ': ' ',
      }
  

def main():

  f = open(sys.argv[1], "r")
  test_cases_number = int(f.readline())
  
  out = open("A.out", 'w')

  for case in xrange(test_cases_number):
    sentence = f.readline()
    out.write("Case #" + str(case + 1) + ": ")
    for l in sentence:
      if l in dic.keys():
        l = dic[l]
        out.write(l)
        print l,
    print
    out.write("\n")
    #out.write("Case #" + str(case + 1) + ": " + country[0:-1] + " is ruled by " + is_ruled_by(country.strip()) + ".\n")

  return 0

if __name__ == '__main__':
  main()

