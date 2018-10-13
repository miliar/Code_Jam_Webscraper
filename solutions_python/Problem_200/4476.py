for t in range(1,int(input())+1):
    n = int(input())
    search = True
    while(search):
        search = False
        for i in range(len(str(n))-1):
            if str(n)[i] > str(n)[i+1]:
                search = True
        n -= 1
    print('Case #{}: {}'.format(t, n+1))
