
import sys
import re
import os
import shutil
import commands
import math

def opening(filename):
  counter=0
  i=1
  f= open (filename,'rU')
  s = open (filename+"out", 'w+')
  text=f.read()
  rows = text.split('\n')
  for row in rows[1:] :
    ruw=row.split(' ')
    for number in range(int(ruw[0]),int(ruw[1])+1): 
        if is_palindrome(math.sqrt(number)) and is_palindrome(number):
            counter+=1
    s.write("Case #"+str(i)+": " + str(counter) +'\n')
    counter=0    
    i+=1
    


def is_palindrome(number):
  numberc=str(number)
  num=numberc.split('.')
  if len(num)>=2:
     if num[1]!='0' : return False
  first=0
  last=-1
  number=num[0]
  length=len(number)
  if length==1: return True
  numb=str(number)
  middle=length/2
  for num in range(1,length):
    
    if numb[first]!=numb[last]:
       return False
    else: 
       first+=1
       last-=1
    if first >= middle: 
       return True
    


def main():
  
  args = sys.argv[1:]

  opening(args[0])
  
if __name__ == "__main__":
  main()
