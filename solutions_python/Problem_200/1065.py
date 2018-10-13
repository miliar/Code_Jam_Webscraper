t=int(input())
for ti in range(1, t+1):
    i = [int(i) for i in list(input())]
    idx = 0
    while True:
        if idx == len(i) - 1:
            break
        if i[idx] > i[idx+1]:
            i[idx] = i[idx]-1
            i[idx+1:] = [9]*len(i[idx+1:])
            idx = 0
        else:
            idx+=1
    i=''.join([str(x) for x in i])
    i=int(i)
    print("Case #{}: {}".format(ti,str(i)))
