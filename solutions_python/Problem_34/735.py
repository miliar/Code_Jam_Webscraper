# coding: utf-8

"""
このスクリプトは、Google Jam Qualification_a用のスクリプトです。
"""

fdic     = open('A-large.dic', 'w')
finput   = open('A-large.in', 'r')

i = 0
for line in finput:
  i = i + 1
  if i == 1:
    numberList = line[:-1].split(' ')
    continue
  if i <= int(numberList[1]) + 1:
    fdic.write(line)
    continue
fdic.close()
finput.close()

#fdic     = open('A-small.dic', 'r')
finput   = open('A-large.in', 'r')
foutput  = open('A-large.out', 'w')
i = 0
for line in finput:
  i = i + 1
  if i <= int(numberList[1]) + 1:
    continue
  group = 0
  rule = []
  charset = []
  for char in line[:-1]:
    if char == "(":
      group = 1
      continue
    if char == ")":
      rule.append(charset)
      charset = []
      group = 0
      continue
    charset.append(char)
    if group == 0:
      rule.append(charset)
      charset = []
      continue
#  print rule
  ok = 0
  for line2 in open('A-large.dic', 'r'):
    j = 0
    err = 0
    for char in line2[:-1]:
      if char in rule[j]:
        j += 1
        continue
      else:
        err = 1
        break
    if err == 0:
      ok += 1
  result = "Case #" + str(i - int(numberList[1]) - 1) + ": " + str(ok) + '\n'
  print result,
  foutput.write(result)

foutput.close()
finput.close()
#fdic.close()


