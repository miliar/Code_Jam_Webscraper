#!/usr/bin/python

f = open('B-large.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('dancing_result_large.txt', 'w')


for i in range (0,numcase):
  line = f.readline()
  linelist = line.split()
  num_people = int(linelist[0])
  surprise = int(linelist[1])
  p = int(linelist[2])
  plist = []
  for j in range (3,3+num_people):
    plist.append(int(linelist[j]))
  answer = 0
  target = (p * 3) - 2
  sp = 0
  #print "p =",p,"target=",target
  for j in range (0,num_people):
    if plist[j] >= target:
      answer = answer + 1
    elif (plist[j] >= (target-2)) and (plist[j] > 0):
      sp = sp + 1  
  #print " pre-answer=",answer," sp=",sp
  if sp >= surprise:
    answer = answer + surprise
  else:
    answer = answer + sp
  answ_sentence = "Case #"+str(i+1)+": "+ str(answer)
  fout.write(answ_sentence)
  fout.write('\n')
  #print "Case #"+str(i+1)+": "+ str(answer)

f.close()
fout.close()




