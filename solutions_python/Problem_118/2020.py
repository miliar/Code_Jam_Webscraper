import sys
import math
f=open(sys.argv[1],"r").read()
f_split=f.split("\n")
square_dict={}
def is_palindrome(integer):
  string_int= str(integer)
  string_reversed=string_int[::-1]
  #print integer
  if string_int==string_reversed:
    return True
  else:
    return False

  
for j in range(1, 10000001):
     sqr_j=j*j
     if is_palindrome(j) and is_palindrome(sqr_j):
       square_dict[sqr_j]=j

sorted_keys= sorted(square_dict, key=square_dict.get)
for i in range(1, int(f_split[0])+1):
   interval=f_split[i].split(" ")
   start = long(interval[0])
   end = long(interval[1])
   count=0
   for key in sorted_keys:
     if key>=start and key<=end:
       count+=1
       
#   for j in range(int(math.sqrt(start)), int(math.sqrt(end)+1)):
#     sqr_j=0
#     if j in square_dict:
#       sqr_j=square_dict[j]
#     else:
#       sqr_j=j*j
#       square_dict[j]=sqr_j
#     #print sqrt_j- int(sqrt_j)
#     count=get_palindrome(j)
#     if is_palindrome(j) and is_palindrome(sqr_j) and sqr_j>=start and sqr_j<=end:
#       #print j, sqr_j
#       count+=1
   print "Case #"+str(i)+": "+str(count)
