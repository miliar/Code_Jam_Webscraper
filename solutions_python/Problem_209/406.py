import numpy as np
def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(long,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"

f_in=open('A-large.in','r')
f_out=open('out_large.txt','w')
output=""
T=readint(f_in)

for i in range (T):
    output+="Case #"+str(i+1)+": "
    N, K=readint_l(f_in)
    RH = []
    for j in range(N):
        RH  +=  [readint_l(f_in)]
    #R, H = zip(*sorted(dat, key=lambda x:x[0], reverse=True))
    RH = map(lambda x:(x[0], x[1]*x[0]*2*np.pi), RH)
    best = -1
    for item in RH:
        curr_try = np.pi*item[0]**2 + item[1]
        RH2 = sorted(filter(lambda x:x[0]<=item[0], RH), key=lambda rh:rh[1], reverse=True)
        RH2.remove(item)
        curr_try += sum(map(lambda x:x[1],RH2[:K-1]))
        best = max(best, curr_try)
    output += '{:.10f}'.format(best)
    output+="\n"

    
f_out.write(output)
print output
f_out.close()
f_in.close()
