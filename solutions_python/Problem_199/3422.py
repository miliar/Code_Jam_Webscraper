t=input()

for i in range(t):
    a=raw_input().split(" ")
    S=list(a[0])
    K=int(a[1])

    finish=list("+"*len(S))

    count=0
    possible=True


    for x in range(len(S)):
        if S[x] == "-":

            if x + K > len(S):
                print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
                possible=False
                break

            else:
                count+=1
                for y in range(K):


                    if S[x+y]=="+":
                        S[x+y]="-"

                    elif S[x+y]=="-":
                        S[x+y]="+"




        if S == finish:
            break
    if possible:
        print "Case #"+str(i+1)+": "+str(count)
