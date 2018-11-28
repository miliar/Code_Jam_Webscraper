fx = [1]*1000001

def solve(x):
    return fx[x]

if __name__=='__main__':
    for i in range(2,1000001):
        s = int(str(i)[::-1])
        if s>=i or i%10==0:
            fx[i] = fx[i-1]+1
        else:
            fx[i]= min(fx[i-1]+1,fx[s]+1)
    print(fx[:20])
    ans = []
    with open('A.in') as f:
        T = int(f.readline())
        for k in range(T):
            x = int(f.readline())
            ans.append(solve(x))

    with open('output.txt','w') as f:
        for k,t in enumerate(ans):
            f.write("Case #"+str(k+1)+": "+"{0}\n".format(t))
