#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     13/04/2013
# Copyright:   (c) Dan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
f1=open("C-small-attempt0.in","r")
f2=open("C-small-attempt0.out","w")
nrcases=f1.readline()

array=[]
for line in f1: # read rest of lines
        array.append([int(x) for x in line.split()])

for count2 in range(1,int(nrcases)+1):
 array2=[]
 array3=[]
 x=0
 A=int(array[count2-1][0])
 B=int(array[count2-1][1])
 for count in range(A,B+1):
    for j in range(0,count+1):
        y2=str(j)
        y=j*j
        if y==count:
            if len(str(j*j))==1:
             array2.append(count)
            z=str(y)
            if len(z)==3 and z[0]==z[2] and y2[0]==y2[1]:
                array2.append(count)
 print("Case #"+str(count2)+":",len(array2),file=f2)


f2.close()









