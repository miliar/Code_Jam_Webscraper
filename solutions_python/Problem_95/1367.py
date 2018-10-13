# Google Code jam Problem A Speaking in Tongues
# Apr. 13, 2012
# Python 3.2.3

import sys
import string

def ReadRules(d):

    encrypted = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z'
    original = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q'

    ency_splitted = encrypted.split()
    orig_splitted = original.split()
    
    len_words = len(ency_splitted)

    for i in range(len_words):
        len_letters = len(ency_splitted[i])
        
        for j in range(len_letters):
            a = ency_splitted[i][j]
            b = orig_splitted[i][j]
            if a not in d:
               d[a] = b
    
    d[' '] = ' '
    d['\n'] = ''
               
    return d
            

def main(inFileName):
   inFile = open(inFileName, mode='r')
   
   numberOfCases = int(inFile.readline())
   
   d = {}
   
   d = ReadRules(d)
   
   #for (k, v) in sorted(d.items()):
   #   print(k + "->" + v + "\n") 

   
   for caseNumber in range(numberOfCases):
      line = inFile.readline()
      
      answer = ''
      
      for i in range(len(line)):
         answer += d[line[i]]
      
      print('Case #' + str(caseNumber+1) + ': ' + answer )
   
if __name__ == '__main__': 
   main(sys.argv[1])
