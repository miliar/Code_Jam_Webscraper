import math

def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"

f_in=open('in.in','r')
f_out=open('out.txt','w')
output=""
T=readint(f_in)

for test in range (T):
    output+="Case #"+str(test+1)+": "
    [n,r,o,y,g,b,v]=readint_l(f_in)
    if (2*r>n or 2*y>n or 2*b>n):
        pr=imp
    else:
        pr=''
        res=[-1 for i in range(n)]
        cols=[r,y,b]
        min_ind=cols.index(min(cols))
        first=(min_ind+1)%3
        sec = (min_ind + 2) % 3
        for i in range (cols[first]):
            res[2*i]=first
        for i in range (cols[sec]):
            ind=(2*(cols[first]-1)+1+2*i)
            if (ind>=n):
                ind=(ind+n%2)%n
            res[ind]=sec
        for i in range(n):
            if (res[i]==-1):
                res[i] = min_ind
        for i in range(n):
            if (res[i]==0):
                pr+='R'
            else:
                if (res[i]==1):
                    pr+='Y'
                else:
                    pr += 'B'
    output+=pr+"\n"

f_out.write(output)
f_out.close()
f_in.close()
