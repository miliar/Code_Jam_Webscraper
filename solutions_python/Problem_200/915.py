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
    n=map(int,readchar_l(f_in))
    d=len(n)
    if n==sorted(n):
        ret=n[:]
    else:
        for j in range(d):
            b=n[:]
            if (b[d-1-j]!=0):
                b[d-1-j]-=1
                if (b[:d-j]==sorted(b[:d-j])):
                    ret=b[:d-j]+[9]*j
                    if(ret[0]==0):
                        ret=ret[1:]
                    break
    output+=''.join(map(str,ret))


    output+="\n"

f_out.write(output)
f_out.close()
f_in.close()
