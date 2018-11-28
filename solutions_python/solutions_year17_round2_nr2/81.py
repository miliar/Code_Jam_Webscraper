def greedy(R,Y,B):
    num=dict(R=R,Y=Y,B=B)
    last=''
    seq=''

    for i in range(R+Y+B):
        choices=[(v,k) for k,v in num.items() if k!=last and v>0]
        if not choices: return 'IMPOSSIBLE'

        m,color=max( choices )
        last=color

        seq+=color

        num[color]=m-1

    if seq[-1]==seq[0]:
        last=seq[0]
        lseq=seq[-3:]
        if lseq[0]==last or lseq[1]==last : return 'IMPOSSIBLE'

        seq=seq[:-3]+lseq[0]+last+lseq[1]

    return seq

def Brute(seq,R,Y,B,N):
    if len(seq)==N:
        print(seq)
        raise ValueError

    last='' if not seq else seq[-1]

    if last!='R' and R:
        Brute(seq+'R',R-1,Y,B,N)

    if last!='Y' and Y:
        Brute(seq+'Y',R,Y-1,B,N)

    if last!='B' and B:
        Brute(seq+'B',R,Y,B-1,N)

T=int(input())
for i in range(T):
    N,R,O,Y,G,B,V=map(int,input().split())
    assert R+Y+B==N
    res=greedy(R,Y,B)
    if res!='IMPOSSIBLE':
        r,y,b=map(lambda x: res.count(x),('R','Y','B'))
        assert r==R
        assert y==Y
        assert b==B
        assert len(res)==N
    print('Case #{}: {}'.format(i+1,res))
