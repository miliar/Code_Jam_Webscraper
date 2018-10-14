'''
Created on 12-Apr-2014

@author: tadikond
'''
import math

def filllookuptable(maxf,C,F,X):
    table=[]
    table.append(0)
    for i in range(maxf):
        table.append(table[i]+C/(2+((i)*F)))
    return table

def gettime(table,farms,C,F,X):
    return table[farms]+X/(2+(farms*F))
     
def cookieclickeralpha(t,fin,fout):
    C,F,X=[float(j) for j in (fin.readline()).split(" ")]
    maxfarms=int(math.floor(X/C))
    lookuptable=filllookuptable(maxfarms,C,F,X)
    result=[]
    for farms in range(maxfarms+1):
        result.append(gettime(lookuptable,farms,C,F,X))
    print("Case #"+str(t)+": "+str(min(result)))
    
    
def main(fin,fout):
    T=int(fin.readline())
    for t in range(T):
        cookieclickeralpha(t+1,fin,fout)
        
if __name__ == '__main__':
    fin=open("B-large.in","r")
    #fin=open("B-small-attempt0.in","r")
    fout=open("B-large.out","w")
    fout.close()
    main(fin,fout)