for _ in range(int(input())):
    n = int(input())
    for i in range(n,0,-1):
        s = str(i)
        t = True
        if(len(s) == 1):
            print("Case #"+str(_+1)+": "+s)
            break
        else:
            for i in range(len(s)-1):
                if s[i]>s[i+1]:
                    t=False
                    break
            if t == True:
                print("Case #"+str(_+1)+": "+s)
                break
