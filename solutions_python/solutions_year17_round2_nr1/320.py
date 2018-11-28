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
    [d,n]=readint_l(f_in)
    speeds=[0 for i in range(n)]
    for i in range(n):
        [start,speed]=readint_l(f_in)
        speeds[i]=float(speed)*(float(d)/float(d-start))
    mini=min(speeds)
    output+=str(mini)+"\n"

f_out.write(output)
f_out.close()
f_in.close()
