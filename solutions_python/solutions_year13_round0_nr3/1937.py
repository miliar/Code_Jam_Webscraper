#!/usr/bin/python -tt
import sys

no_of_test_case=0
test_case=[]
output=[]

def read_file(input_file):
  global no_of_test_case
  global test_case
  f=open(input_file,'rU')
  first=True
  for line in f:
    if first:
      no_of_test_case_str=line
      no_of_test_case=int(no_of_test_case_str)
      first=False
    else:
      test_case.append(line)
  f.close()

def write_file(out_file):
  f=open(out_file,'w')
  for i in range(len(output)):
    str="Case #%d: %s\n" %(i+1,output[i])
    f.write(str)
  f.close()  

def palindrone(n):
  str_n=str(n)
  str_n_rev=str_n[::-1]
  return str_n==str_n_rev
    
def fair_and_sq(line):
  line1=line.split()
  a=int(line1[0])
  b=int(line1[1])
  a1=int(a**(0.5))
  b1=int(b**(0.5))+1
  count=0
  num=a1-1
  for i in range(b1-a1+1):
    num=num+1
    if palindrone(num):
      sq=int(num**2)
      if palindrone(sq) and sq>=a and sq<= b:
        count=count+1
  return count

def main():
  input_file='input.txt'
  out_file='output.txt'
  read_file(input_file)
  for i in range(no_of_test_case):
    output.append(fair_and_sq(test_case[i]))
  
  write_file(out_file)
if __name__=='__main__':
  main()

    