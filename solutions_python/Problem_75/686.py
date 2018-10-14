#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

def process_combine(text, combines):
  for combine in combines:
    text = text.replace(combine['from'], combine['to'])
  return text

def process_opposed(text, opposed_list):
  for rule in opposed_list:
    m = re.search('%s.*?%s' % (rule['src'], rule['dst']), text)
    if m:
      return ''
  return text

case = int(sys.stdin.readline())
for c in range(0, case):
  parts = sys.stdin.readline().strip().split(' ')

  # make combination list
  combines = []
  (num_combines, parts) = (int(parts[0]), parts[1:])
  for i in range(0, num_combines):
    data = parts[i]
    base = data[:2]
    rev = data[:2][::-1]
    combines.append({'from':base,'to':data[2]})
    if base != rev:
      combines.append({'from':rev,'to':data[2]})
  parts = parts[num_combines:]

  # make opposed list
  opposed_list = []
  (num_opposed_list, parts) = (int(parts[0]), parts[1:])
  for i in range(0, num_opposed_list):
    data = parts[i]
    opposed_list.append({'src':data[0], 'dst':data[1]})
    if data[0] != data[1]:
      opposed_list.append({'src':data[1], 'dst':data[0]})
  parts = parts[num_opposed_list:]

  # data to be processed
  line = parts[1]

  # main routine
  result = ''
  for ch in line:
    result += ch
    result = process_combine(result, combines)
    result = process_opposed(result, opposed_list)

  print "Case #%d: %s" % (c+1, '[%s]' % (', '.join(list(result)),))
