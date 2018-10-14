#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Python 2.6.4

def Magicka(d,s1,s2,num):  
  l = [str(x) for x in s2]
  for key in d.keys(): 
    m = str(key)
  #print m
  Z= [x for x in m]
  Z.reverse()
  Z = "".join(Z)
  n = d[m] 
  #print Z
  #print n
  len1 = len(s2)
  s4,s5 = '',''
  j = 0
  if len(s1) > 0:
    v,w = [g for g in s1]
  else: v,w = '',''
  for i in range(len1):
    s4 += l[j]
    s5 += s4[-1] 
    #print '1st s5', s5       
    if s4[-2:] != m and s4[-2:] != Z:
     if v != '' and w != '':
      if v in s5 and w in s5:
        s5 = ''
    elif len(s5)>1:
      if s5[-2:] == m or s5[-2:] == Z:
       s5=s5.replace(s5[-2:],n)               
    j += 1
  s9 = [b for b in s5] ; s9 = ", ".join(s9) 
  print "Case #%s: [%s]" % (num,s9)
  outfile = open('magicka_s.txt','a')
  outfile.write("Case #%s: [%s]\n" % (num,s9))


def main(filename):
  infile = open(filename,'r')
  T = int(infile.readline())
  for num in range(1,T+1):
    L = [ d for d in infile.readline().strip().split(' ')] #; print L       
    C = int(L[0])   
    val_c = []
    for i in range(1,C+1): 
      val_c.append(L[i])
    #print 'val_c is',val_c
    D = int(L[C+1])  ; val_d = [] 
    for j in range(L.index(L[-2 + (-D)]),L.index(L[-2])):
      val_d.append(L[j])
    #print 'val_d is', val_d
    N = int(L[-2])
    s2 = L[-1]    
    #get_dico(val_c)
    t = rs1(val_d)
    u = get_dico(val_c)
    Magicka(u.next(),t.next(),s2,num)

def rs1(val_d):
  if len(val_d) == 0:
   yield ''
  else:
    for it in val_d:
      if it != None:
        yield it
      else: yield ''
    
def get_dico(val_c):
  d2 = []
  if len(val_c) != 0:
    for elem in val_c:    
      f1 = [d for d in elem] 
      g = "".join(f1[:-1]) 
      d = {} 
      d[g] = f1[-1]
      d2.append(d)
  else:
    d = {'':''}
    d2.append(d)    
    #print d2
  for ele in d2:
    yield ele

if __name__ == "__main__":
  main('B-small-attempt0.in') 
