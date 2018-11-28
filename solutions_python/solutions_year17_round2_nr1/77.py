from codejam import checkEq

def calc(now,speed,initial):
    assert now>speed
    t=initial/(now-speed)

    return t*now

def check(now,horses,D):

    for speed,initial in horses:
        if speed>=now : break

        if calc(now,speed,initial)<D: return False

    return True

def bisearch(D,horses):
    head=0
    tail=D*max(horses)[0]

    while not checkEq(head,tail,1e-6):
        mid=(head+tail)/2

        if check(mid,horses,D): head=mid
        else: tail=mid

    return (head+tail)/2

def init():
    D,N=map(int,input().split())
    horses=[]

    for i in range(N):
        initial,speed=map(int,input().split())

        horses.append((speed,initial))

    horses.sort()

    return D,horses

T=int(input())
for i in range(T):
    print('Case #{}: {}'.format(i+1,bisearch(*init())))
