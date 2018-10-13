#!/usr/bin/python

lines = [line.strip() for line in open('D-large.in')]
num_case = [int (i) for i in lines[0].split()][0]
for case in range(num_case):
   naomi_line = lines[2 + case * 3]
   ken_line = lines[3 + case * 3]
   n_num = [float (i) for i in naomi_line.split()]
   k_num = [float (i) for i in ken_line.split()]
   n_num = sorted(n_num)
   k_num = sorted(k_num)

  # win1 = [i for i, j in zip(n_num, k_num) if i > j]
  # win2 = [i for i, j in zip(n_num, reversed(k_num)) if i > j]
  # ans1 = max(len(win1), len(win2))
   k1 = 0
   k2 = 0
   win_lie = 0
   while k2 < len(n_num):
     if k1 >= len(n_num):
       break
     if n_num[k1] > k_num[k2]:
       win_lie += 1
       k2 += 1
     k1 += 1

   c1 = 0
   c2 = 0
   win = 0
   while c1 < len(n_num):
     if c2 >= len(n_num):
       break
     if k_num[c2] < n_num[c1]:
       win += 1
     else:
       c1 += 1
     c2 += 1
   ans2 = win
   print "Case #" + str(case + 1) + ": " + str(win_lie) + " " + str(ans2)
   
     
    
