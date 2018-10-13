def bsum(l):
    out=0
    for x in l:
        out^=x
    return out

def powerbool(n):
    if n==0:
        return [[]]
    out=[]
    for sub in powerbool(n-1):
        out.append([True]+sub)
        out.append([False]+sub)
    return out

inpf=open('input.txt')
T=int(inpf.readline()[:-1])
out=''

for case in range(1,T+1):
    answer='NO'
    N=int(inpf.readline())
    candy=list(map(int,inpf.readline().split()))
    possibles=powerbool(N-1)[:-1]
    most=0
    for boolsub in possibles:
        a=[]
        b=[candy[-1]]
        for i in range(N-1):
            if boolsub[i]:
                a.append(candy[i])
            else:
                b.append(candy[i])
        if bsum(a)==bsum(b):
            value=max(sum(a),sum(b))
            if value>most:
                most=answer=value
    out+='Case #{}: {}\n'.format(case,answer)

outf=open('output.txt',mode='w')
print(out[:-1],end='',file=outf)
outf.close()
inpf.close()
