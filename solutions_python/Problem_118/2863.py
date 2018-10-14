from math import sqrt
import string, sys
input_file = open('C-small-attempt1.in')
output_file = open('output.txt','r+')
def is_square_palindome(x):
    y = sqrt(x)
    if y%1==0:
        yrev = str(int(y))
    else:
        yrev = str(y)
    if x<10:
        return y%1==0
    else:
        xrev = str(int(x))
        return yrev==yrev[::-1] and  xrev==xrev[::-1]
    

for case in range(int(input_file.readline())):
        count =0
        A,B= map(int,input_file.readline().split(" "))
        for i in range(A,B+1):
            if is_square_palindome(i):
                count+=1
        output_file.write("Case #{0}: {1}\n".format(case+1,count))

