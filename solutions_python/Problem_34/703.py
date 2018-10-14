#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,re

class Allien():
  def __init__(self):
    if sys.argv.__len__() != 2:
        print "No file to read !"
        return None
    try:
      f = open(sys.argv[1],'r')
      ff = open('allien_result.out','w')
    except:
      return None
    self.numbers = [int(x) for x in re.search("([0-9]+).([0-9]+).([0-9]+)" ,(f.readline())).groups()]
    tab = [x.strip() for x in f.readlines()]
    self.words,self.cases = " ".join(tab[:self.numbers[1]]),tab[self.numbers[1]:]
    self.cases = [x.replace('(','[') for x in self.cases]
    self.cases = [x.replace(')',']') for x in self.cases]
    out = []
    for x in xrange(self.numbers[2]):
      out.append('Case #%s: %s\n'%(x+1,self.find_me(x)))
    ff.writelines(out)
    f.close()
    ff.close()
      
  def find_me(self,x):
    return len(re.findall(self.cases[x],self.words))
    
Allien()
  



