T = int(input())
for t in range(T):
    D, N = [int(i) for i in input().split()]
    mx = 0
    for n in range(N):
        pos, speed = [int(i) for i in input().split()]
        #print(pos, speed, (D - pos)/speed)
        mx = max((D - pos)/speed, mx)
    print("Case #%i: %f" % (t+1, D/mx))