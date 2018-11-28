#!/usr/bin/env python

import os 
import sys

fd_in = open(sys.argv[1], 'r')
name_out = sys.argv[1].split('.in')[0] + '.out' 
fd_out = open(name_out, 'w')

data = fd_in.read().split('\n')

if len(data) == 1:
   print 'file empty'
   sys.exit()

T = int(data[0])
if T > 100 or T < 1:
   print 'ERROR in T'
   sys.exit()

if len(data) < (10*T)+1:
   print 'No enough data'
   sys.exit()

cases = 1
i = 1
while cases <= T:
   set1 = {}
   set2 = {}
   
   answer1 = int(data[i])
   i = i + 1
   set1[1] = data[i]
   i = i + 1
   set1[2] = data[i]
   i = i + 1
   set1[3] = data[i]
   i = i + 1
   set1[4] = data[i]
   i = i + 1
   
   answer2 = int(data[i])
   i = i + 1
   set2[1] = data[i]
   i = i + 1
   set2[2] = data[i]
   i = i + 1
   set2[3] = data[i]
   i = i + 1
   set2[4] = data[i]
   i = i + 1

   if answer1 < 1 or answer1 > 4 or answer2 < 1 or answer2 > 4:
      print "ERROR en some answer row"
      break
      
   sum1 = 0
   sum2 = 0
   test_l1 = []
   test_l2 = []
   for k in range (0,4):
       sum1 = sum1 +sum(int(j) for j in set1.values()[k].split(' ')) 
       test_l1.extend(j for j in set1.values()[k].split(' '))
   for k in range (0,4):
       sum2 = sum2 +sum(int(j) for j in set2.values()[k].split(' ')) 
       test_l2.extend(j for j in set2.values()[k].split(' '))

   if sum1 != sum(range(1,17)) or sum2 != sum(range(1,17)):
       print "sum no OK"
       break
   if len(set(test_l1)) != 16 or len(set(test_l2)) != 16:
      print 'Number Repeated in list' 
      break
 
   l =list(set(set1[answer1].split(' ')).intersection(set2[answer2].split(' ')))
   
   if len(l) == 0:
         print 'Case #' + str(cases) + ': ' + 'Volunteer cheated!' 
         fd_out.write('Case #' + str(cases) + ': ' + 'Volunteer cheated!\n')
   if len(l) == 1:
         print 'Case #' + str(cases) + ': ' + l[0]
         fd_out.write('Case #' + str(cases) + ': ' + l[0] + '\n') 
   if len(l) > 1:
         print 'Case #' + str(cases) + ': ' + 'Bad magician!'
         fd_out.write('Case #' + str(cases) + ': ' + 'Bad magician!\n')


   cases = cases + 1

fd_in.close()
fd_out.close()