import random
import copy

def main():  
  voc = prepare_voc()
  lines = read_in()
  
  f = open('A-small-out.txt', 'w')
  for i in range(0, len(lines)):
    a = lines[i]
    b = translate(a, voc)
    f.write("Case #%d: %s\n" % (i+1, b))
  
  f.close()
    
def translate(word, voc):
  tr_word = ''
  for i in range(0, len(word)):
    tr_word += voc[word[i]]
  return tr_word

def prepare_voc():
  a = "zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
  b = "qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

  abc = {}
  for i in range(0, len(a)):
    abc[a[i]] = b[i]
  
  return abc

def read_in():
  f = open('A-small.in', 'r')
  lines = f.read().splitlines()
  lines = lines[1:]
  f.close()
  return lines

if __name__ == '__main__':
  main()