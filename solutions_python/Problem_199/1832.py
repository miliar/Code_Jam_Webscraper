def flip(c,i,k):
    s=""
    if((i+k)>len(c)):
        return "failed"
    for j in range(i,(i+k)):
        if(c[j]=='+'):
            s+='-'
        else:
            s+='+'
    return (c[:i] + s + c[i+k:])

def main():
    t = input()
    l=0
    while l<t:
        r=0
        c,k = map(str,raw_input().split())
        k = int(k)
        c = c[::-1]
        flag = 0
        for i in range(0,len(c)):
            if c[i]=='-':
                z = flip(c,i,k)
                if(z=="failed"):
                    flag=1
                    print "Case #%d: IMPOSSIBLE"%(l+1)
                    break
                else:
                    r+=1
                    c = z
        if flag ==0:
            print "Case #%d: %d"%(l+1,r)
        l+=1
if __name__ == '__main__':
    main()