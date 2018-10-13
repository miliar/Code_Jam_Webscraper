inpf=open('input.txt')
N=int(inpf.readline()[:-1])
out=''

def other(bot):
    if bot=='O':
        return 'B'
    return 'O'

def sign(x):
    if x==0:
        return 0
    if x>0:
        return 1
    return -1

for case in range(1,N+1):
    data=inpf.readline().split()[1:]
    data=[(data[i],int(data[i+1])) for i in range(0,len(data),2)]
    pos={'O':1,'B':1}
    t=0
    for i in range(len(data)):
        bot=data[i][0]
        dest=data[i][1]
        dist=abs(pos[bot]-dest)
        time=dist+1
        for button in data[i+1:]:
            obot=button[0]
            if obot!=bot:
                odest=button[1]
                odist=abs(pos[obot]-odest)
                if odist<=time:
                    pos[obot]=odest
                else:
                    pos[obot]-=sign(pos[obot]-odest)*time
                break
        t+=time
        pos[bot]=dest
    out+='Case #{}: {}\n'.format(case,t)

outf=open('output.txt',mode='w')
print(out[:-1],end='',file=outf)
outf.close()
inpf.close()
