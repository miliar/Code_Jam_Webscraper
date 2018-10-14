#!/usr/bin/python

#f = open('c_fairsquare_input.txt')
f = open('C-large-1.in')
inputline = f.readline()
numcase = int(inputline)

def is_palindrome(num):
  stringval = str(num)
  slen = len(stringval)
  if slen == 1:
    return True
  else:
    #print "checking ",stringval
    for i in range(0,slen/2):
      if stringval[i] != stringval[slen-i-1]:
        #print "i=",i," stringval[i]=",stringval[i]
        return False  

  return True

answer_set = []
#up to32 for small input set
for i in range(1,10000001):
  if is_palindrome(i):
    square = i * i
    if is_palindrome(square):
      answer_set.append(square)


fout = open('c_large1_result.txt', 'w')



for i in range (0,numcase):
  inputline = f.readline()
  linelist = inputline.split()
  a = int(linelist[0])
  b = int(linelist[1])
  total = 0
  for val in answer_set:
    if val >= a and val <= b:
      total += 1

  answ_sentence = "Case #"+str(i+1)+": "+ str(total)
  fout.write(answ_sentence)
  fout.write('\n')
  print answ_sentence