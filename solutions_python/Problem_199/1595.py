t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [str(s) for s in input().split(" ")]
    ind = 0
    ope = 0
    m = int(m)
    nlist = []
    for e in n:
        nlist.append(e)
    l = {'+','-'}
    while ind < len(nlist) - m + 1:
        if nlist[ind] == '-':
            nlist[ind] = '+'
            for j in range(ind+1, ind+m):
                nlist[j] = list(l - set(nlist[j]))[0]
            ope += 1
        ind += 1
    for f in range(-m+1,0):
        if nlist[f] == '-':
            ope = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i, ope))
