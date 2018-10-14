
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
f_out=open('out.txt','w')
output=""
T=readint(f_in)

for i in range (T):
    output+="Case #"+str(i+1)+": "
    D, N=readint_l(f_in)
    dat = []
    for j in range(N):
        dat  +=  [readint_l(f_in)]
    dat.append((0, float('inf')))
    K, S = zip(*sorted(dat, key=lambda x:x[0], reverse=True))
    
    while True:
        if len(K)==1:
            break
        t0 = (D - K[0])*1.0/S[0]
        speed = min(S[1], (D-K[1])*1./t0)
        K = K[1:]
        S = [speed] + list(S[2:])
    output += '{:.8f}'.format(speed)
    output+="\n"

f_out.write(output)
print output
f_out.close()
f_in.close()
