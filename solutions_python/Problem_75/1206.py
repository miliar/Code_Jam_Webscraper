#!/usr/bin/python

import re

i = open("B-large.in", "r")

T = int(i.readline())

for n_line in range(1, T+1):
  line = i.readline()

  a_line = line.split()

  C = int(a_line[0])
  D = int(a_line[C+1])
  N = int(a_line[C+D+2])

  patterns_c = []
  replaces_c = []

  if C > 0:
    for a in range(1, C+1):
      patterns_c.append(a_line[a][0:2])
      patterns_c.append(a_line[a][0:2][::-1])

      replaces_c.append(a_line[a][2:3])
      replaces_c.append(a_line[a][2:3])

  if D > 0:
    for a in range(C+2, C+D+2):
      patterns_c.append(".*"+a_line[a][0]+".*"+a_line[a][1])
      patterns_c.append(".*"+a_line[a][1]+".*"+a_line[a][0])

      replaces_c.append("")
      replaces_c.append("")

  elements = a_line[C+D+3]
  string = elements[0]

  for e in range(1, N):
    string += elements[e]

    for a in range(len(patterns_c)):
      string = re.sub(patterns_c[a], replaces_c[a], string)

  answer = "Case #" + str(n_line) + ": ["
  for a in range(len(string)):
    if a > 0:
      answer += ", " + string[a]
    else:
      answer += string[a]

  answer += "]"
  #print line,
  print answer

  #raw_input("Presione para continuar...")
