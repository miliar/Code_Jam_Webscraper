def f(l):
    begin={'O':1,'B':1}
    last=l[0][0]
    lasttime=0
    result=0
    for k in l:
        robot=k[0]
        if robot==last:
            lasttime+=1+abs(k[1]-begin[robot])
            result+=1+abs(k[1]-begin[robot])
            begin[robot]=k[1]
        else:
            temp=abs(k[1]-begin[robot])
            temp=max(temp,lasttime)
            lasttime=1+temp-lasttime
            result+=lasttime
            begin[robot]=k[1]
            last=robot
    return result
def main():
    s=input()
    T=int(s)
    for i in range(T):
        s=input()
        s=s.split(' ')
        k=int(s[0])
        s=s[1:]
        l=[(s[2*i],int(s[2*i+1]))  for i in range(k)]
        print('Case #{0}: {1}'.format(i+1,f(l)))
main()
