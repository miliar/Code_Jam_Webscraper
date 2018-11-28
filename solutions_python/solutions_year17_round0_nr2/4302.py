#!/usr/bin/env python3.5

def tidy(line):
  for k in range(1,len(line)):
    if(line[k-1]>line[k]):
      return 0
  return 1

def Solve(j,line):
  if(len(line)==1):
    print ("Case #"+str(j)+": "+line)
  # elif()
  else:
    while(tidy(line)==0):
      for i in range(1,len(line)):
        if(line[i-1]>line[i]):
          if(i==1):
            if(line[0]=='1'):
              line="9"*(len(line)-1)
            else:
              line=chr(ord(line[0])-1)+"9"*(len(line)-1)
          else:
            line=line[:i-1]+chr(ord(line[i-1])-1)+"9"*(len(line)-i)
          break
        # print(line)
      # ll=int(line)
      # ll-=1
      # line=str(ll)
    print("Case #"+str(j)+": "+line)

  return

ip=open("B-large.in",'r')
no = ip.readline()
no = int(no)

for i in range(0,no):
  line = ip.readline()
  line = line.replace("\n","")
  # line = line.split(' ')
  j=i+1
  Solve(j,line)
  # print(tidy(line))
