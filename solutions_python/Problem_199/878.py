def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(l): return ' '.join(map(str,l))
imp="IMPOSSIBLE"

f_in=open('in.txt','r')
f_out=open('out.txt','w')
output=""
T=readint(f_in)
for i in range (T):
    output+="Case #"+str(i+1)+": "
    line=read_l(f_in)
    k=int(line[1])
    s=plus_min_str_to10_l(line[0])
    n=len(s)
    counter=0
    for i in range(n-k+1):
        if (s[i]==0):
            counter+=1
            for j in range(k):
                s[i+j]^=1
    if(s==[1]*n):
        output+=str(counter)
    else:
        output += imp
    output+="\n"

f_out.write(output)
f_out.close()
f_in.close()
