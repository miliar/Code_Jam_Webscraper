#!/usr/bin/python -tt
import sys
  
def read_file():
  f=open('input.txt','rU')
  lines = [line.strip() for line in f]
  no=int(lines[0])
  k=1
  output=[]
  for value in range(no):
    string=''
    l= lines[k].split()
    N=int(l[0])
    M=int(l[1])
    k=k+1
    for val in range(N):
      string=string+lines[k]+' '
      k=k+1
    string=string[:-1:2]
    output.append(lawnmover(string,N,M))
   
  f.close()
 
  f=open('output.txt','w')
  for i in range(no):
    str="Case #%d: %s\n" %(i+1,output[i])
    f.write(str)
  f.close()
  
def lawnmover(string,N,M):      
  i=0
  j=0
  dict={}
  output='YES'
  for char in string:
    dict[j]='F'
    j=j+1
  for char in string:
    if dict[i]=='F':
      if char=='2': 
        dict[i]='T'
      else:
        ssc=string[i%M:(N-1)*M+1+(i%M):M]
        if ssc.find('2')==-1:
          index=i%M
          while index<=(N-1)*M +1:
            dict[index]='T'
            index=index+M
        else:
          ssc=string[i-i%M:M+(i-i%M):1]
          if ssc.find('2')==-1:
            index=i-i%M
            while index < M+(i-i%M):
              dict[index]='T'
              index=index+1
          else:    
            dict[i]='F'
            output='NO'
            break
    i=i+1
  return output
read_file()

  