#N*N algorithm
def tidy(N):
    data = list(N)
    ok = True
    for i in range(len(data)-1):
        if ord(data[i]) > ord(data[i+1]):
            data[i] = chr(ord(data[i])-1)
            for j in range(i+1,len(data)):
                data[j] = '9'
            ok = False
            break
    if ok:
        return int("".join(data))
    else:
        return tidy("".join(data))

N = int(input())
for i in range(N):
    print(("Case #%d: %d" % (i+1,tidy(input()))))
