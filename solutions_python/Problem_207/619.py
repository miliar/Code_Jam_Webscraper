inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    args=list(((inp.readline()).rstrip()).split())
    N = int(args[0])
    R = int(args[1])
    O = int(args[2])
    Y = int(args[3])
    G = int(args[4])
    B = int(args[5])
    V = int(args[6])
    #for small
    if N/2>=R and N/2>=Y and N/2 >=B and N/2>=O and N/2>=G and N/2>=V and B>=O and Y>=V and R>=G:
        ans = ''
        if R>Y and R>B:
            fr = 'R'
            while R>0 or Y>0 or B>0:
                ans+=fr
                if fr=='R':
                    R-=1
                    if Y>=B:
                        fr='Y'
                    elif B>Y:
                        fr='B'
                elif fr=='Y':
                    Y-=1
                    if R>=B:
                        fr='R'
                    elif B>R:
                        fr='B'
                else:
                    B-=1
                    if R>=Y:
                        fr='R'
                    elif Y>R:
                        fr='Y'
        elif B>Y and B>R:
            fr = 'B'
            while R>0 or Y>0 or B>0:
                ans+=fr
                if fr=='R':
                    R-=1
                    if Y>=B:
                        fr='Y'
                    elif B>Y:
                        fr='B'
                elif fr=='Y':
                    Y-=1
                    if R>=B:
                        fr='R'
                    elif B>R:
                        fr='B'
                else:
                    B-=1
                    if R>=Y:
                        fr='R'
                    elif Y>R:
                        fr='Y'
        elif Y>R and Y>B:
            fr = 'Y'
            while R>0 or Y>0 or B>0:
                ans+=fr
                if fr=='R':
                    R-=1
                    if Y>=B:
                        fr='Y'
                    elif B>Y:
                        fr='B'
                elif fr=='Y':
                    Y-=1
                    if R>=B:
                        fr='R'
                    elif B>R:
                        fr='B'
                else:
                    B-=1
                    if R>=Y:
                        fr='R'
                    elif Y>R:
                        fr='Y'
        else:
            if R>0:
                fr = 'R'
            elif Y>0:
                fr = 'Y'
            else:
                fr ='B'
            while R>0 or Y>0 or B>0:
                ans+=fr
                if fr=='R':
                    R-=1
                    if Y>=B:
                        fr='Y'
                    elif B>Y:
                        fr='B'
                elif fr=='Y':
                    Y-=1
                    if R>=B:
                        fr='R'
                    elif B>R:
                        fr='B'
                else:
                    B-=1
                    if R>=Y:
                        fr='R'
                    elif Y>R:
                        fr='Y'
        if ans[0]==ans[-1]:
            t1 = ans[-1]
            t2 = ans[-2]
            ans = ans[:-2]
            ans+=t1
            ans+=t2
        out.write("Case #" + str(i+1) + ": " + ans+ "\n")
    else:
        out.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")