#!/usr/bin/python

#f = open('b_lawnmower_input.txt')
f = open('B-large.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('b_large_result.txt', 'w')

for i in range (0,numcase):
  inputline = f.readline()
  linelist = inputline.split()
  n = int(linelist[0])
  m = int(linelist[1])
  lawn = []
  result = "YES"
  #print "n=",n," m=",m
  for j in range (0,n):
    inputline = f.readline()
    linelist = inputline.split()
    row = []
    #print "linelist=",linelist
    for k in range (0,m):
      row.append(int(linelist[k]))
    #print "row",str(row)
    lawn.append(row)

  for j in range (0,n):
    rowmin = min(lawn[j])
    rowmax = max(lawn[j])
    #unequal heights
    if rowmin != rowmax:
      for k in range (0,m):
        square = lawn[j][k]
        #check vertically since the cut couldn't came horizontally
        if square != rowmax:
          for r in range(0,n):
            if lawn[r][k] > square:
              result = "NO"
  answ_sentence = "Case #"+str(i+1)+": "+ result
  fout.write(answ_sentence)
  fout.write('\n')
  print answ_sentence