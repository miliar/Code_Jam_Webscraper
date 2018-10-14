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
    [n,q]=readint_l(f_in)
    horse=[0 for i in range(n)]
    mat = [0 for i in range(n)]
    quest = [0 for i in range(q)]
    for i in range (n):
        horse[i]=readint_l(f_in)
    for i in range (n):
        mat[i]=readint_l(f_in)
    for i in range (q):
        quest[i]=readint_l(f_in)
    dists=[mat[i][i+1] for i in range(n-1)]
    min_upto=[0 for i in range(n)]
    for i in range(1,n):
        listi=[0 for k in range(i)]
        for j in range(i):
            leng=sum(dists[j:i])
            if (horse[j][0]<leng):
                listi[j]=2**64
            else:
                listi[j]=min_upto[j]+float(leng)/float(horse[j][1])
        min_upto[i]=min(listi)
    output+=str(min_upto[n-1])+"\n"

f_out.write(output)
f_out.close()
f_in.close()
