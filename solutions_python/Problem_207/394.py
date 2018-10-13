import  random
for i in range(input()):
    n, R, O, Y, G, B, V = (map(int, raw_input().split()))
    if R<=n/2 and Y<=n/2 and B<=n/2:
        ans = [""]*n
        if R>=Y and Y>=B:
            k=0
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        elif R>=B and B>=Y:
            k=0
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        elif B>=R and R>=Y:
            k=0
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        elif B>=Y and Y>=R:
            k=0
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        elif Y>=B and B>=R:
            k=0
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        elif Y>=R and R>=B:
            k=0
            while True:
                if Y==0:
                    break
                ans[k] = "Y"
                Y-=1
                k+=2
                if k>=n:
                    k=1
                if Y==0:
                    break
            while True:
                if R==0:
                    break
                ans[k] = "R"
                R-=1
                k+=2
                if k>=n:
                    k=1
                if R==0:
                    break
            while True:
                if B==0:
                    break
                ans[k] = "B"
                B-=1
                k+=2
                if k>=n:
                    k=1
                if B==0:
                    break
            print "Case #" + str(i+1) + ": " + "".join(ans)
        
    else:
        print "Case #" + str(i+1) + ": IMPOSSIBLE"
    
