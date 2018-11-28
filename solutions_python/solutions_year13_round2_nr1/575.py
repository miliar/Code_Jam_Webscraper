# motes[0]
#
#
#
#
#



def solve(a,motes):
    l=len(motes)
    if l==0:
        return 0
    for i in range(l):
        if a > motes[i]:
            a+=motes[i]
        else:
            break
    if i == l-1 and a>motes[i]:
        return 0
    elif i== l-1 and a<=motes[i]:
        return 1
    if a>1:
        ans=min(1+solve(a+a-1,motes[i:]),1+solve(a,motes[i:l-1]))
    else:
        ans=1+solve(a,motes[i:l-1])
    return ans


T=int(raw_input())

for x in range(1,T+1):
    a, n = [int(i) for i in raw_input().split()]
    motes= [int(i) for i in raw_input().split()]
    motes.sort()
    ans=solve(a,motes)
    print "Case #"+str(x)+": " + str(ans)
