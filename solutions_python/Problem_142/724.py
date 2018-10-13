# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:02:27 2013

@author: slonny
"""
from sys import argv
from collections import Counter
from collections import OrderedDict
import numpy


script, filename = argv

file = open(filename)

T = int(file.readline())


for t in xrange(T):
  N = int(file.readline())
  
  data=[]
  data_counter=[]
  first=1  
  new_list=[]
  old_list=[]
  bad_game=False
  
  for n in xrange(N):
      if first>2 and old_list!=new_list:
          bad_game=True 
      else:
          old_list=new_list
          temp_data=list(file.readline().rstrip())
          prev_char=[]
          new_list=[]
          count_list=[]
          out_data=[]
          for i in temp_data:
              if prev_char!=i:
                  new_list.append(i)
                  count_list.append(1)
                  prev_char=i
              else:
                  count_list[-1]=count_list[-1]+1
          data.append(new_list)
          data_counter.append(count_list)
          first=first+1
          
     
  if (first>2 and old_list!=new_list) or bad_game:
      print "Case #%d: Fegla Won" % (t + 1)   
  else:
      total_moves=0
      #print data
      #print data_counter
      for j in xrange(len(new_list)):
          letter=new_list[j]
          letter_counter=[]
          for i in xrange(N):
              counter=data_counter[i][j]
              letter_counter.append(counter)
        
          #print letter
          #print letter_counter
          avg_counter=round(numpy.mean(letter_counter))
          moves=[abs(avg_counter-x) for x in letter_counter]
          
          moves2=sum(letter_counter)-N*min(letter_counter)
          
          min_moves=min(sum(moves), moves2)
          #print min_moves
          total_moves+=min_moves
          
      print "Case #%d: %d" % (t + 1, total_moves)
          
      

      
  #print data      
      

  

     


