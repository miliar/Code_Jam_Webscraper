T = int(input())

for t in range(T):
    N = list(input().strip())

    index = -1
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            index = i
            break
    for i in range(index,-1,-1):
        if N[i] > N[i+1]:
            N[i+1] = '9'
            N[i] = chr(ord(N[i])-1)
    if index >= 0:
        N[index+1:] = ['9'] * (len(N) - (index+1))
    print("Case #%d: %d" % ( t+1, int(''.join(N)) ))

