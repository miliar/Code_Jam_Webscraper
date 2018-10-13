def main():
    t = input()
    l = 0
    while l<t:
        res=0.000000
        d,n = map(int,raw_input().split())
        while n>0:
            k,s = map(int,raw_input().split())
            if (d-k+0.000000)/s > res:
                res = (d-k+0.000000)/s
            n-=1
        print "Case #%d: %f"%(l+1,d/(res+0.00000))
        l+=1
if __name__=="__main__":
    main()