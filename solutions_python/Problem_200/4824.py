# import math
# class Solver:
#   def demo(self):
#       while True:
#           a = int(input("a "))
#           b = int(input("b "))
#           c = int(input("c "))
#           d = b ** 2 - 4 * a * c
#           if d>=0:
#               disc = math.sqrt(d)
#               root1 = (-b + disc) / (2 * a)
#               root2 = (-b - disc) / (2 * a)
#               print(root1, root2)
#           else:
#               print("error")
#
# Solver().demo()
#=======================================================================
# import logging
# logging.basicConfig(filename='test.log',level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')
# def adder(a,b):
#   return a+b
# def sub(a,b):
#   return a-b
# def mul(a,b):
#   return a*b
# def div(a,b):
#   return a/b
#
# numa= 9
# numb=10
#
# addval=adder(numa,numb)
# logging.debug('Add: {}+{}={}'.format(numa,numb,addval))
# subval=sub(numa,numb)
# logging.debug('Add: {}-{}={}'.format(numa,numb,subval))
# mulval=mul(numa,numb)
# logging.debug('Add: {}*{}={}'.format(numa,numb,mulval))
# divVal=div(numa,numb)
# logging.debug('Add: {}/{}={}'.format(numa,numb,divVal))
#Alt+J ==>  multiple selection whereas Ctrl+slash to comment out a block of code
#=========================================================================
# import os
# path = "C:\\Users\\Administrator\\PycharmProjects\\untitled1\\src"
# #file_name = os.path.join(path, "A-large-practice.in")
# file_name = os.path.join(path, "A-small-practice.in")
# file_name1= os.path.join(path, "output.in")
# my_file = open(file_name,"r")
# openfile = open(file_name1, 'w')

# def sheepCount(number):
#   N=1 #counter
#   final=[]
#   puray=[]
#   haza=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#   evaluate="0,1,2,3,4,5,6,7,8,9"
#   storedNumber=int(number)
#   while N>0:
#     loop=storedNumber*N
#     if storedNumber==0:
#       return "INSOMNIA"
#     final.append(str(loop))
#     #print("RUN",loop,N)
#     for i in range(0,len(str(loop))):
#       if (str(loop)[i] in evaluate) and (str(loop)[i] not in puray):
#         puray.append(str(loop)[i])
#         puray.sort()
#     if puray==haza:
#       #print("YES!!",puray)
#       break
#     N+=1
#   #print(final)
#   return loop
#
# #x=input("Enter the number:")
# counter=1
# for line in my_file:
#     #print(sheepCount(line),counter)
#     counter+=1
#     #openfile.write("Case #"+line+": "+str(sheepCount(line))+"\n")
#     openfile.write("Case #{}: {}\n".format(counter-1,str(sheepCount(line))))
#     # format of output is Case #x: y
# openfile.close()
# my_file.close()
import os
path = "C:\\Users\\Administrator\\PycharmProjects\\untitled1\\src"
#file_name = os.path.join(path, "A-large-practice.in")
file_name = os.path.join(path, "B-small-attempt1.in")
file_name1= os.path.join(path, "a.in")
my_file = open(file_name,"r")
openfile = open(file_name1, 'w')

def counter(x):
  All=[]
  Lister=[]
  number=int(x)
  for i in range(0,number+1):
    no=str(i)
    if len(no)==1:
      All.append(int(no))
    if len(no)>1:
      for j in range(0,len(no)):
        try:
          if no[j]<no[j+1] or no[j]==no[j+1]:
            Lister.append(True)
          else:
            Lister.append(False)
        except:
          if False in Lister:
            Lister=[]
            break
          elif no[len(no)-2]<no[len(no)-1] or no[len(no)-2]==no[len(no)-1]:
            All.append(int(no))

    #or (j==len(no)-1):
  All.sort()
  y=len(All)
  #print(check)
  return All[y-1]

#number=input("Enter:")
#print(counter(number))
Counter=1
for line in my_file:
  #print(sheepCount(line),counter)
  Counter+=1
  # #openfile.write("Case #"+line+": "+str(sheepCount(line))+"\n")
  openfile.write("Case #{}: {}\n".format(Counter-1,str(counter(line))))
  # format of output is Case #x: y
openfile.close()
my_file.close()
