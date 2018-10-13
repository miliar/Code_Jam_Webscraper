#!/usr/bin/python

import sys


def le_dic():
  try:
    f = open('dic.txt','rU')
  except IOError:
    print 'IOError: erro ao abrir arquivo. dic.txt'
    sys.exit(1)

  dic = {}
  for line in f:
    dic[line[0]] = line[2]

  f.close()
  
  return dic
  
def translate(s,dic):
  #if s[-1] == '\n' :
  #  s = s[0:-1]
  line = ''
  for i in range(len(s)):
    try:
      let = dic[s[i]]
    except KeyError:
      let = s[i]
    line = line + let
  return line
  
def main(args):
  ft_in = args[0];
  if len(args) > 1 :
    ft_out = args[1];
  else:
    ft_out = 'a.out'

  dic = le_dic()

  try:
    fin = open(args[0],'rU')
  except IOError:
    print 'IOError: erro ao abrir arquivo.'
    sys.exit(1)
  lines = fin.readlines();
  fin.close()
  
  try:
    fout = open(ft_out,'w')
  except IOError:
    print 'IOError: erro ao abrir arquivo.'
    sys.exit(1)
  
  
  T = int(lines[0])
  for i in range(1,T+1):
    t_line = translate(lines[i],dic)    
    fout.write('Case #%d: %s' % (i, t_line))
  fout.close()

  return
  
if __name__ == '__main__':
  args = sys.argv[1:]
  usage = "usage: file_in [file_out]"
  if not args:
    print usage;
    sys.exit(1)
  main(args)
