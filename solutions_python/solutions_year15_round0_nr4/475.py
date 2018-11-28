def solve(x,r,c):
    if x==1:
        return True
    elif x==2:
        if r*c%2==0 :
            return True
        else:
            return False
    elif x==3:
        if r==3 or c==3 :
            if min(r,c)==1:
                return False
            else:
                return True
        else:
            return False
    elif x==4:
        if max(r,c)<=3 :
            return False
        else:
            if r>c: r,c=c,r
            if r<=2:
                return False
            else:
                return True
    else:
        return False

if __name__=='__main__':
    ans = []
    with open('input.txt')as f:
        T = int(f.readline())
        for i in range(T):
            x,r,c = [int(t) for t in f.readline().split()]
            ans.append(solve(x,r,c))
    with open('output.txt','w') as f:
        for i,t in enumerate(ans):
            if t:
                f.write("Case #"+str(i+1)+": "+"GABRIEL\n")
            else:
                f.write("Case #"+str(i+1)+": "+"RICHARD\n")
    
