import sys

fileName = "A-large"
sys.stdin = open(fileName+".in", 'r')
output = open(fileName+".out", 'w')

T = int(input())
for case in range(1,T+1):

    ###################### input data ###############################

    N,P = input().split(" ")
    print("N="+N+", P="+P)
    N,P = int(N),int(P)
    G = input().split(" ")
    print("G="+str(G))

    ######################### compute answer ##################################

    a = [0]*P
    for x in G:
        a[int(x)%P] += 1
    print("a="+str(a))

    if P==2:
        answer = a[0] + (a[1]+1)//2
        print("Case #%d:" % case, answer)
        print("Case #%d:" % case, answer, file = output)
    elif P==3:
        x,y,z = a[0],min(a[1],a[2]),abs(a[1]-a[2])
        answer = x + y + (z+2)//3
        print("Case #%d:" % case, answer)
        print("Case #%d:" % case, answer, file = output)
    elif P==4:
        if a[2]%2==0:
            w,x,y,z = a[0],a[2]//2,min(a[1],a[3]),abs(a[1]-a[3])
            answer = w + x + y + (z+3)//4
            print("Case #%d:" % case, answer)
            print("Case #%d:" % case, answer, file = output)
        else:
            w,x,y,z = a[0],a[2]//2,min(a[1],a[3]),abs(a[1]-a[3])
            answer = w + x + y + (z+5)//4
            print("Case #%d:" % case, answer)
            print("Case #%d:" % case, answer, file = output)

    ###########################################################################
