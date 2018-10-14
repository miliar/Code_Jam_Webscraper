#!/usr/bin/python

import os
import sys
import math

def read_input_NN(fn =""):
  fh = open(fn, "r")
  lines = map(lambda x: x.strip(), fh.readlines())
  fh.close()
  goog_N = lines[0]
  l_strings = lines[1:]
  return(l_strings)

def truncate_s(s1 = "", left1 = "w", right1 = "m"):
  if left1 in s1:
    s1 = s1[s1.index(left1):]
  if right1 in s1:
    s1 = s1[:s1.rindex(right1)+1]
  return(s1)

def remove_bad(string1 = "abc",bad1 = "bc"):
  bad1 = set(bad1)
  list1 = list(string1)
  list2 = []
  for i in list1:
    if i not in bad1:
      list2+=[i]
  return("".join(list2))

def keep_good(string1 = "abc",good1 = "bc"):
  good1 = set(good1)
  list1 = list(string1)
  list2 = []
  for i in list1:
    if i in good1:
      list2+=[i]
  return("".join(list2))

def condense_dups(l1 = [('w', 1), ('w', 1), ('e', 1), ('e', 1)]):
  letter = "x"
  l2 = []
  for i in l1:
    letter_new = i[0]
    count_new = i[1]
    if letter_new == letter:
      l2[-1][1]+=count_new
    else:
      l2 += [i]
    letter = letter_new
  return(l2)

def all_indices(string, sub, listindex, offset):
  # call as l = allindices(string, sub, [], 0)
  # http://code.activestate.com/recipes/499314/
  if (string.find(sub) == -1):
    return listindex
  else:
    offset = string.index(sub)+offset
    listindex.append(offset)
    string = string[(string.index(sub)+1):]
    return allindices(string, sub, listindex, offset+1)

def allindices(string, sub, listindex, offset):
  # call as l = allindices(string, sub, [], 0)
  # http://code.activestate.com/recipes/499314/
  if (string.find(sub) == -1):
    return listindex
  else:
    offset = string.index(sub)+offset
    listindex.append(offset)
    string = string[(string.index(sub)+1):]
    return allindices(string, sub, listindex, offset+1)

def list_prod(l1=[1,2,3]):
  prod1 = 1
  for i in l1:
    prod1 = prod1*i
  return(prod1)

def count_times(l1=[]):
  counter1 = 0
  let_ct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  match_str = "welcome to code jam"
  case_str = "".join(map(lambda x: x[0],l1))	
  for i00 in all_indices(case_str,match_str[0],[],0):
    let_ct[0] = l1[i00][1]
    for i01 in all_indices(case_str[i00:],match_str[1],[],i00):
      let_ct[1] = l1[i01][1]
      for i02 in all_indices(case_str[i01:],match_str[2],[],i01):
        let_ct[2] = l1[i02][1]
        for i03 in all_indices(case_str[i02:],match_str[3],[],i02):
          let_ct[3] = l1[i03][1]
          for i04 in all_indices(case_str[i03:],match_str[4],[],i03):
            let_ct[4] = l1[i04][1]
            for i05 in all_indices(case_str[i04:],match_str[5],[],i04):
              let_ct[5] = l1[i05][1]
              for i06 in all_indices(case_str[i05:],match_str[6],[],i05):
                let_ct[6] = l1[i06][1]
                for i07 in all_indices(case_str[i06:],match_str[7],[],i06):
                  let_ct[7] = l1[i07][1]
                  for i08 in all_indices(case_str[i07:],match_str[8],[],i07):
                    let_ct[8] = l1[i08][1]
                    for i09 in all_indices(case_str[i08:],match_str[9],[],i08):
                      let_ct[9] = l1[i09][1]
                      for i010 in all_indices(case_str[i09:],match_str[10],[],i09):
                        let_ct[10] = l1[i010][1]
                        for i011 in all_indices(case_str[i010:],match_str[11],[],i010):
                          let_ct[11] = l1[i011][1]
                          for i012 in all_indices(case_str[i011:],match_str[12],[],i011):
                            let_ct[12] = l1[i012][1]
                            for i013 in all_indices(case_str[i012:],match_str[13],[],i012):
                              let_ct[13] = l1[i013][1]
                              for i014 in all_indices(case_str[i013:],match_str[14],[],i013):
                                let_ct[14] = l1[i014][1]
                                for i015 in all_indices(case_str[i014:],match_str[15],[],i014):
                                  let_ct[15] = l1[i015][1]
                                  for i016 in all_indices(case_str[i015:],match_str[16],[],i015):
                                    let_ct[16] = l1[i016][1]
                                    for i017 in all_indices(case_str[i016:],match_str[17],[],i016):
                                      let_ct[17] = l1[i017][1]
                                      for i018 in all_indices(case_str[i017:],match_str[18],[],i017):
                                        let_ct[18] = l1[i018][1]
                                        #for i019 in all_indices(case_str[i018:],match_str[19],[],i018):
                                        #  let_ct[] = l1[i019][1]
                                        #print let_ct
                                        counter1 = (counter1 + list_prod(let_ct)) % 10000
  return(counter1)

def fill_zeros(int1=1,zeros=6):
  str1 = str(int1)
  diff1 = zeros-len(str1)
  if diff1 >0:
    return("0"*diff1+str1)
  else:
    return(str1)

def qa(fn="sample"):
  l1 = read_input_NN(fn)
  l2 = []
  for i in l1:
    l2 += [truncate_s(i,"w","m")]
  l3 = []
  for i in l2:
    l3 += [keep_good(i,"welcome to code jam")]
  l3 = map(lambda x: list(x),l3)
  l3 = map(lambda x: map(lambda y: [y,1], x) , l3)
  l3 = map(lambda x: condense_dups(x), l3)
  l3 = map(lambda x: count_times(x), l3)
  #print l3
  return(l3)

l1 = qa(fn="C-small-attempt0.in")
#print l1

fh = open("out.txt","w")
for (ctr,sol) in enumerate(l1):
  print >> fh, "Case #"+str(ctr+1)+": "+ fill_zeros(sol % 10000,4)

fh.close()
