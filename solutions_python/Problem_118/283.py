#!/usr/bin/env python
import os
import sys
import time

tStart = time.time()

#filename = 'input.txt' 
#filename = 'C-small-attempt0.in' 
#filename = 'C-large-1.in' 
filename = 'C-large-2.in' 

ifile = open(filename)
data  = ifile.read()
ifile.close()

lines   = data.splitlines()
n_cases = int(lines[0])
lines   = lines[1:]

print n_cases


#----------------------------------------------------------
def check_palindrome(N):

  N_tmp = N
  N_dig = []
  while(N_tmp > 0):
    N_dig.append(N_tmp%10)
    N_tmp = int(N_tmp/10)
  
  is_palindrome = 1
  for k in xrange(int(len(N_dig)/2)):
    if N_dig[k] != N_dig[-k-1]:
      is_palindrome = 0
  
  return is_palindrome


#----------------------------------------------------------
def get_square_palindromes(ndigits, verbose=0):

  palindromes = []

  if ndigits == 1:
    palindromes = [1,4,9]
    if verbose == 1:
      print 1, 1
      print 4, 2
      print 9, 3
  elif ndigits == 2:
    for x in xrange(1,10):
      N  = x*10+x
      N2 = N**2
      if check_palindrome(N2) == 1:
        palindromes += [N2]
        if verbose == 1:
          print N2, N
  elif ndigits < 5:
    ydigits = int((ndigits-1)/2)
    for x in xrange(1,10):
      for y in xrange(10**ydigits):
        yd = [int(y/10**k)%10 for k in xrange(ydigits)]
        yr = [yd[-k-1] for k in xrange(len(yd))]
        if ndigits%2 == 0: dd = [x]+yd+yr    +[x]
        else:              dd = [x]+yd+yr[1:]+[x]
        N  = sum([x*10**k for k,x in enumerate(dd)])
        N2 = N**2
        if check_palindrome(N2) == 1:
          palindromes += [N2]
          if verbose == 1:
            print N2, N
  else:
    ndigits_tmp = ndigits
    add_middle  = 0

    if ndigits%2 == 1:
      add_middle = 1
      ndigits_tmp -= 1

    ydigits = int((ndigits_tmp-1)/2)
    if add_middle == 1: c_cases = [0,1,2]
    else:               c_cases = [0]
    for y in xrange(2**ydigits):
      yd = [int(y/2**k)%2 for k in xrange(ydigits)]
      yr = [yd[-k-1] for k in xrange(len(yd))]
      for nc,c in enumerate(c_cases):
        if add_middle == 0: dd = [1]+yd+yr+[1]
        if add_middle == 1: dd = [1]+yd+[c]+yr+[1]
        if sum(dd) < 10:
          N  = sum([x*10**k for k,x in enumerate(dd)])
          N2 = N**2
          if check_palindrome(N2) == 1:
            palindromes += [N2]
            if verbose == 1:
              print N2, N, sum(dd)

    dd1 = [2]+[0 for k in xrange(ndigits-2)]+[2]
    dds = [dd1]
    if ndigits%2 == 1:
      dd2 = [x for x in dd1]
      dd2[int(ndigits/2)] = 1
      dds.append(dd2)

    for dd in dds:
      N  = sum([x*10**k for k,x in enumerate(dd)])
      N2 = N**2
      if check_palindrome(N2) == 1:
        palindromes += [N2]
        if verbose == 1:
          print N2, N, sum(dd)

  return palindromes
#----------------------------------------------------------
def find_pos(vector,x):
  pmin = 0
  pmax = len(vector)-1
  pp   = int((pmax+pmin)/2)
  while pmax-pmin > 1:
    if vector[pp] < x: pmin = pp
    else:              pmax = pp      
    pp   = int((pmax+pmin)/2)

  return pmin,pmax

#----------------------------------------------------------


max_digits  = 1
palindromes = []
for digits in xrange(1,max_digits+1):
  print digits
  palindromes += get_square_palindromes(digits,0)
palindromes.sort()
max_palindrome = max(palindromes)


cases_results = []
for nc in xrange(n_cases):
  line = lines[nc].split()
  A    = int(line[0])
  B    = int(line[1])

  while B > max_palindrome:
    max_digits     += 1
    palindromes    += get_square_palindromes(max_digits)
    palindromes.sort()
    max_palindrome  = max(palindromes)

  pos1min,pos1max = find_pos(palindromes,A)
  pos2min,pos2max = find_pos(palindromes,B)

  result = pos2max - pos1min +1 - int(palindromes[pos1min] < A)  - int(palindromes[pos2max] > B) 
  cases_results.append(result)
    
  print A,B,result

print ''

ofile = open('output.txt','w')
for k,solution in enumerate(cases_results):
  text = 'Case #%d: %d '%(k+1,solution)
  print text
  ofile.write(text+'\n')
ofile.close()

print '\n Run time = ' + str((time.time() - tStart))



