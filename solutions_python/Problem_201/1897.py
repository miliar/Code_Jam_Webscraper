def main():
    t=input()
    l=0
    while l<t:
        n,k = map(int,raw_input().split())
        if n==k:
            x,y=0,0
        else:
            s=[]
            s.append(n)
            while k>1:
                z = s[0]
                s.pop(0)
                if z % 2 == 0:
                    s.append(z / 2)
                    s.append(z / 2 - 1)
                else:
                    s.append(z / 2)
                    s.append(z / 2)
                k-=1
                s.sort(reverse=True)
            z=s[0]
            if z % 2 == 0:
                x = (z / 2)
                y = (z / 2 - 1)
            else:
                x = (z / 2)
                y = (z / 2)
            if y==-1:
                y=0
        print "Case #%d: %d %d"%(l+1,x,y)
        l+=1

if __name__ == '__main__':
    main()