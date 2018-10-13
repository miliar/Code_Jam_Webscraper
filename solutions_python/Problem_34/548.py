#! /usr/bin/env python

import sys

def solve(mydict,input_word,index):
  count = 0
  if type(input_word[index]) is list:
    for k in range(len(input_word[index])):
      if input_word[index][k] in mydict:
        if index == len(input_word) - 1:
          count += 1
        else:
          count += solve(mydict[input_word[index][k]],input_word,index+1)
  else:
    if input_word[index] in mydict:
      if index == len(input_word) - 1:
        count += 1
      else:
        count += solve(mydict[input_word[index]],input_word,index+1)
  return count
                                                                                
f_in = open(sys.argv[1], 'r')
f_out = open('%s.out' % sys.argv[1], 'w')
info = f_in.readline()
info = info.split()
info[0] = int(info[0])
info[1] = int(info[1])
info[2] = int(info[2])
# read all words in alien language
dict = {}
for i in range(info[1]):
  current = dict
  word = f_in.readline()
  word = list(word)
  for j in range(len(word)):
    if word[j] in current:
      current = current[word[j]]
    else:
      if j < info[0] - 2:
        current[word[j]] = {}
      elif j < info[0] - 1:
        current[word[j]] = []
      else:
        current.append(word[j])
        break
      current = current[word[j]]
# read in each testcase and solve
i = 1
while i <= info[2]:
  str = f_in.readline()
  str = list(str)
  input_word = []
  current_letter = input_word
  for j in range(len(str)):
    if str[j] == '(':
      current_letter.append([])
      current_letter = current_letter[-1]
    elif str[j] == ')':
      current_letter = input_word
    elif str[j] == '\n':
      pass
    else:
      current_letter.append(str[j])
  total = solve(dict,input_word,0)
  f_out.write('Case #%d: %d\n' % (i, total))
  print 'Case #%d: %d' % (i, total)
  i += 1
f_in.close()
f_out.close()
