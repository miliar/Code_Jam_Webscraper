from __future__ import division

import os
import os.path, time
import itertools

def cor(cake,r,c):
        for i in range(0,r):
                for j in range(0,c):
                        if cake[i][j]!="?":
                                for k in range(0,j):
                                        if cake[i][k]=="?":
                                                cake[i][k]=cake[i][j]
                for j in range(c-1,-1,-1):
                        if cake[i][j]!="?":
                                for k in range(c-1,j,-1):
                                        if cake[i][k]=="?":
                                                cake[i][k]=cake[i][j]
        for j in range(0,c):
                for i in range(0,r):
                        if cake[i][j]!="?":
                                for k in range(0,i):
                                        if cake[k][j]=="?":
                                                cake[k][j]=cake[i][j]
                for i in range(r-1,-1,-1):
                        if cake[i][j]!="?":
                                for k in range(r-1,i,-1):
                                        if cake[k][j]=="?":
                                                cake[k][j]=cake[i][j]
         
        return cake
        

        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("A-small-attempt0.in")
#fw=open("A-small-attempt0.out","w")
fo=open("A-large.in")
fw=open("B-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        r,c=fo.readline().rstrip().split()
        r=int(r)
        c=int(c)
        cake=[]
        for i in range(0,r):
                linecake=[]
                line=fo.readline().rstrip()
                for j in range(0,c):
                        linecake.append(line[j])
                cake.append(linecake)

        cakenew=cor(cake,r,c)
        print str(k+1)      
        fw.write("Case #"+ str(k+1)+": ")
        fw.write("\n") 
        for i in range(0,r):
                for j in range(0,c):
                        fw.write(cakenew[i][j])
                fw.write("\n")       
fw.close()        
        
                





