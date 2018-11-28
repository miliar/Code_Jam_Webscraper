# @author: Raviphol Sukhajoti
# LANG : PY
# TASK : B
from __future__ import print_function
import sys,math,triangle

def IO():
    global fin
    infile = raw_input("Input File : ")
    outfile = raw_input("Output File : ")
    if len(infile) > 3 and infile[-3:] == '.in': 
        infile = infile[:-3]
    if not outfile == '' :
        if len(outfile) > 4 and outfile[-4:] == '.out': outfile = outfile[:-4]
        sys.stdout = open(outfile+'.out','w')
    fin = open(infile+'.in','r') 

def complete():
    sys.stdout = sys.__stdout__
    fin.close()
    print("completed.")
    
def notSat(i,j):
    for ii in range(i,j+1):
        if m[ii] > 0: return True
    return False

def buy(i,j):
    global ans
    ans += 1
    for ii in range(i,j+1): m[ii] -= 1
    if (i+j)//2 > i:
        if notSat(i,(i+j)//2): buy(i,(i+j)//2)
        if notSat(((i+j)//2)+1,j):  buy(((i+j)//2)+1,j)

if __name__ == '__main__':
    IO()
    T = int(fin.readline())
    for t in range(1,T+1):
        ans = 0
        P = int(fin.readline())
        m = [(P-int(x)) for x in fin.readline().split(' ')]
        for i in range(P): fin.readline()
        if notSat(0,(2**P)-1): buy(0,(2**P)-1)
        print('Case #%d:'%t,ans)
    complete()
    
    